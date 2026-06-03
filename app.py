import os
import math
import time
import threading
from urllib.parse import urlparse, urljoin

import fitz  # PyMuPDF
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_from_directory,
    flash,
    jsonify,
)
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_paginate import Pagination
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import generate_password_hash, check_password_hash

UPLOAD_FOLDER = "library"
APP_KEY = os.environ.get("DOCKER_PDF_SERVER_KEY", "super_secret_key")
APP_USER = os.environ.get("DOCKER_PDF_SERVER_USER", "admin")
APP_PASSWORD = os.environ.get("DOCKER_PDF_SERVER_PASSWORD", "password")
ALLOWED_EXTENSIONS = {"pdf", "epub"}

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = APP_KEY

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = None

app.app_context().push()


class EnvAdminUser(UserMixin):
    """Represents the env-var-configured admin; never stored in the DB."""
    id = 0

    @property
    def username(self):
        return APP_USER

    role = "admin"

    def get_id(self):
        return "0"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    role = SelectField(
        "Role",
        choices=[
            ("reader", "Reader"),
            ("admin", "Admin"),
            ("maintainer", "Maintainer"),
        ],
        validators=[DataRequired()],
    )
    submit = SubmitField("Add User")


@login_manager.user_loader
def load_user(user_id):
    if int(user_id) == 0:
        return EnvAdminUser()
    return db.session.get(User, int(user_id))


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def safe_redirect(target):
    ref = urlparse(request.host_url)
    test = urlparse(urljoin(request.host_url, target))
    return test.scheme in ("http", "https") and ref.netloc == test.netloc


def generate_thumbnail(pdf_path, thumbnail_path):
    doc = fitz.open(pdf_path)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(0.25, 0.25))
    pix.save(thumbnail_path, jpg_quality=70)
    doc.close()


# ── Directory cache ──────────────────────────────────────────────────────────
# Replaces per-request os.listdir + 2000 individual getmtime() stat() calls
# with a single os.scandir() pass, cached for 15 s. Upload/delete invalidate
# it immediately so the UI stays consistent.

_CACHE_TTL = 15.0
_cache_lock = threading.Lock()
_cache: dict = {"stamp": 0.0, "pdfs": [], "thumbs": set()}


def _scan_library(folder: str) -> tuple[list[tuple[str, float]], set[str]]:
    """Return ([(name, mtime), ...], {thumb_names}) from a single scandir pass."""
    now = time.monotonic()
    with _cache_lock:
        if now - _cache["stamp"] < _CACHE_TTL:
            return _cache["pdfs"], _cache["thumbs"]
        pdfs: list[tuple[str, float]] = []
        thumbs: set[str] = set()
        with os.scandir(folder) as it:
            for entry in it:
                if not entry.is_file():
                    continue
                if entry.name.endswith(".pdf"):
                    pdfs.append((entry.name, entry.stat().st_mtime))
                elif entry.name.endswith((".jpg", ".png")):
                    thumbs.add(entry.name)
        _cache.update(stamp=now, pdfs=pdfs, thumbs=thumbs)
        return pdfs, thumbs


def _invalidate_cache() -> None:
    with _cache_lock:
        _cache["stamp"] = 0.0


@app.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username == APP_USER and password == APP_PASSWORD:
            login_user(EnvAdminUser())
            next_page = request.args.get("next")
            return redirect(next_page if next_page and safe_redirect(next_page) else url_for("index"))
        db_user = User.query.filter_by(username=username).first()
        if db_user and db_user.check_password(password):
            login_user(db_user)
            next_page = request.args.get("next")
            return redirect(next_page if next_page and safe_redirect(next_page) else url_for("index"))
        flash("Invalid username or password.", "danger")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.errorhandler(500)
def internal_server_error(e):
    return (
        jsonify(
            {
                "error": "Sorry, the app encountered a 500 internal server error. It just doesn't like you today."
            }
        ),
        500,
    )


@app.route("/library")
@login_required
def index():
    page = request.args.get("page", 1, type=int)
    per_page = max(4, min(120, request.args.get("per_page", 12, type=int)))
    sort_order = request.args.get("sort", "newest")
    upload_folder = app.config["UPLOAD_FOLDER"]

    pdf_entries, thumb_set = _scan_library(upload_folder)
    reverse = sort_order != "oldest"
    pdf_files = [n for n, _ in sorted(pdf_entries, key=lambda x: x[1], reverse=reverse)]

    total_files = len(pdf_files)
    final_page = math.ceil(total_files / per_page) if total_files else 1
    start = (page - 1) * per_page
    pdf_files_slice = pdf_files[start:start + per_page] if start < total_files else []
    pagination = Pagination(page=page, per_page=per_page, total=total_files)

    files = [
        {"file": f, "thumbnail": f"{f}.jpg" if f"{f}.jpg" in thumb_set else (f"{f}.png" if f"{f}.png" in thumb_set else "pdf-file.png")}
        for f in pdf_files_slice
    ]

    return render_template(
        "index.html",
        files=files,
        pagination=pagination,
        last=final_page,
        sort_order=sort_order,
        per_page=per_page,
    )


@app.route("/search")
@login_required
def search():
    query = request.args.get("query", "").strip()
    page = request.args.get("page", 1, type=int)
    per_page = max(4, min(120, request.args.get("per_page", 12, type=int)))
    sort_order = request.args.get("sort", "newest")
    upload_folder = app.config["UPLOAD_FOLDER"]

    pdf_entries, thumb_set = _scan_library(upload_folder)
    query_lower = query.lower()
    reverse = sort_order != "oldest"
    pdf_files = [
        n for n, _ in sorted(
            [(n, m) for n, m in pdf_entries if query_lower in n.lower()],
            key=lambda x: x[1],
            reverse=reverse,
        )
    ]

    total_files = len(pdf_files)
    final_page = math.ceil(total_files / per_page) if total_files else 1
    start = (page - 1) * per_page
    pdf_files_slice = pdf_files[start:start + per_page] if start < total_files else []
    pagination = Pagination(page=page, per_page=per_page, total=total_files)

    files = [
        {"file": f, "thumbnail": f"{f}.jpg" if f"{f}.jpg" in thumb_set else (f"{f}.png" if f"{f}.png" in thumb_set else "pdf-file.png")}
        for f in pdf_files_slice
    ]

    return render_template(
        "index.html",
        files=files,
        query=query,
        pagination=pagination,
        last=final_page,
        sort_order=sort_order,
        per_page=per_page,
    )


@app.route("/upload", methods=["POST"])
@login_required
def upload_file():
    if current_user.role not in ["admin", "maintainer"]:
        flash("Unauthorized access!", "danger")
        return redirect(url_for("index"))

    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = file.filename
        ext = filename.rsplit(".", 1)[1].lower()
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        if ext == "epub":
            pdf_filename = filename.rsplit(".", 1)[0] + ".pdf"
            pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], pdf_filename)
            try:
                doc = fitz.open(file_path)
                pdf_bytes = doc.convert_to_pdf()
                doc.close()
                with open(pdf_path, "wb") as f:
                    f.write(pdf_bytes)
            except Exception:
                os.remove(file_path)
                return render_template(
                    "error.html",
                    error_message="Could not convert EPUB to PDF. The file may be malformed.",
                )
            os.remove(file_path)
            filename = pdf_filename
            file_path = pdf_path

        try:
            thumbnail_path = os.path.join(app.config["UPLOAD_FOLDER"], filename + ".jpg")
            generate_thumbnail(file_path, thumbnail_path)
        except Exception:
            error_message = (
                "Could not generate thumbnail. The PDF may be malformed. "
                "You may still view it if your client supports it."
            )
            return render_template("error.html", error_message=error_message)

        _invalidate_cache()
        return redirect(url_for("index"))


@app.route("/library/<filename>")
@login_required
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/delete", methods=["POST"])
@login_required
def delete_file():
    if current_user.role not in ["admin", "maintainer"]:
        flash("Unauthorized access!", "danger")
        return redirect(url_for("index"))

    filename = request.form["filename"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        for thumb_ext in (".jpg", ".png"):
            thumbnail_path = os.path.join(app.config["UPLOAD_FOLDER"], filename + thumb_ext)
            if os.path.exists(thumbnail_path):
                os.remove(thumbnail_path)
        _invalidate_cache()
        flash("File deleted successfully.", "success")
    else:
        flash("File not found.", "error")
    return redirect(url_for("index"))


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if current_user.role != "admin":
        flash("Unauthorized access!", "danger")
        return redirect(url_for("index"))

    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        role = form.role.data
        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "danger")
        else:
            new_user = User(username=username, role=role)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully.", "success")
            return redirect(url_for("admin"))

    users = User.query.all()
    return render_template("admin.html", form=form, users=users)


@app.route("/delete_user", methods=["POST"])
@login_required
def delete_user():
    if current_user.role != "admin":
        flash("Unauthorized access!", "danger")
        return redirect(url_for("index"))

    user_id = request.form["user_id"]
    user = db.session.get(User, user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully.", "success")
    else:
        flash("User not found.", "error")
    return redirect(url_for("admin"))


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    db.create_all()
    app.run(port=3030, debug=False)
else:
    with app.app_context():
        db.create_all()