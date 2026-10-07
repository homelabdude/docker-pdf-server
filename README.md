# Docker PDF Server

![CI Status Badge](https://github.com/homelabdude/docker-pdf-server/actions/workflows/ci.yml/badge.svg)
![GitHub License](https://img.shields.io/github/license/homelabdude/docker-pdf-server)
[![Docker Image Version](https://img.shields.io/docker/v/a0ne/docker-pdf-server)](https://hub.docker.com/r/a0ne/docker-pdf-server)
![Docker Pulls](https://img.shields.io/docker/pulls/a0ne/docker-pdf-server)

Welcome to the Docker PDF Server! This project provides a responsive and ultra-minimalist PDF server running on Docker. 
Built with Flask and HTML, it offers a no-nonsense, straightforward way to upload, delete, view, search, and serve PDFs and EPUBs.

> **EPUB support** is available from the 1.6.0 beta releases onwards. Uploaded EPUB files are automatically converted to PDF before storing.

## Why Docker PDF Server?

I developed this server out of a personal need for a quick, e-book-like viewing experience for my PDF library. Unlike
document organizers like Paperless-ngx or eBook focused apps like Calibre-web, Kavita etc., this server focuses solely
on delivering a simple way to upload, browse, search, and access PDF e-books for reading. When you click on a file,
it is served as is. From 1.6.0 betas, you can upload both PDF and EPUB files.

It is actually functionally similar to any typical client app for a NAS. However, this server brings the convenience of
browser-based access, allowing for quick viewing and on-the-go reading on any device.

<img src="https://raw.githubusercontent.com/homelabdude/docker-pdf-server/refs/heads/main/screenshots/Home.png" alt="Alt text" style="width:70%;">

## What Docker PDF Server is not

- This server is not designed to be a comprehensive document organizer like Paperless-ngx.
- It lacks a database or any form of grouping/bookmarking system and relies solely on file system, potentially limiting
  scalability if you want to have anything over a few 1000 files.
- Session-based authentication is implemented, with optional [OIDC single sign-on](#single-sign-on-oidc). It is advisable not to expose the server publicly without additional
  security. I use this with Authentik running on my reverse-proxy.
- Currently, it lacks a folder system. Although this feature is simple enough to do and could be considered for future
  implementation.
- Error handling although basic covers all scenarios.

## Getting Started

Just run the below docker command replacing the username, password and secret with your preferred values, and you should
be up and running.

```
docker run -e DOCKER_PDF_SERVER_USER=<your-username> \
 -e DOCKER_PDF_SERVER_PASSWORD=<your-password> \
 -e DOCKER_PDF_SERVER_KEY=<your-random-secret-key> \
 -v /Users/writable/host/path/pdf-library:/app/library/ \
 -v /Users/writable/host/path/user-db:/app/instance/ \
 -p 3040:5000 ghcr.io/homelabdude/docker-pdf-server:latest
```

You can then access the app by going to `http://localhost:3040`

> Note: Starting the container without setting the env vars will start it with the default key, username and password

### User Management

Any version after 1.4.x, the default admin user configured through env vars `DOCKER_PDF_SERVER_USER` and `DOCKER_PDF_SERVER_PASSWORD`
can add additional admins, maintainers and readers

- **Admin** - Can add other users
- **Maintainer** - Cannot add users but can upload, delete files
- **Reader** - Can only read files

> Note: To switch users, use the logout button in the top-right corner of the app.

Admins can change a user's role at any time from the role dropdown in the Users table.

### Single Sign-On (OIDC)

You can let users sign in through an OpenID Connect provider such as Authelia, Authentik, Keycloak, or Pocket ID.
SSO is enabled when `OIDC_CLIENT_ID`, `OIDC_CLIENT_SECRET` and `OIDC_ISSUER` are all set. A **Sign in with SSO** button then
appears below the username/password form, which keeps working as before.

| Env var | Default | Description |
|---|---|---|
| `OIDC_CLIENT_ID` | — | Client ID registered with your provider |
| `OIDC_CLIENT_SECRET` | — | Client secret registered with your provider |
| `OIDC_ISSUER` | — | Issuer URL, e.g. `https://auth.example.com`. `/.well-known/openid-configuration` is appended to discover the provider's endpoints |
| `OIDC_REDIRECT_URI` | `<app-url>/login/oidc/callback` | Callback URL to register with your provider. Only needed if the app can't work out its public URL |
| `OIDC_AUTO_CREATE_USERS` | `false` | Create an account on first sign-in for users who don't have one. New accounts are **Readers**; an admin can promote them |
| `OIDC_SCOPES` | `openid email profile` | Scopes to request |
| `OIDC_PROVIDER_NAME` | `SSO` | Label for the sign-in button, e.g. `Authelia` |
| `OIDC_USERNAME_CLAIM` | `preferred_username` | Claim used as the username |
| `OIDC_EMAIL_CLAIM` | `email` | Claim used as the email address |
| `OIDC_NAME_CLAIM` | `name` | Claim used as the display name |

When someone signs in through SSO, they are matched to an account in this order:

1. **Already linked**: the account previously linked to that SSO identity (the provider's `sub` claim).
2. **Matching email**: an unlinked account with the same email address. Only used when the provider says the email is verified (`email_verified`).
3. **Matching username**: an unlinked account with the same username.
4. **New account**: if `OIDC_AUTO_CREATE_USERS` is `true`, a new Reader account. Otherwise sign-in is refused.

A matched account is linked to the SSO identity and keeps its role and password. Email and display name are refreshed
from the provider on every SSO sign-in. To give an existing user SSO access, set their email in the **Add User** form, or
make sure their username matches the one at your provider. The env-var admin account is never linked to SSO.

> **Security note:** username matching trusts your provider's usernames. Only use a provider where users can't pick a
> username that belongs to someone else here, such as a self-hosted provider where you create the accounts.

### Building and Running Locally for Development

- Get started by creating a python venv in this directory by running `python3 -m venv venv` or `python -m venv venv`
- Then run `source venv/bin/activate` on Linux/macOS.
- If on Windows, run `env/Scripts/activate.bat` in CMD or `env/Scripts/Activate.ps1`for PowerShell.
- Then run `pip install -r requirements.txt`
- After that, you can start your app server for development by running `python3 app.py` or `python app.py`
- If you want to build a docker image you can do so by running `docker build . -t docker-pdf-server:latest`

> Note: The default [Flask Secret Key](https://explore-flask.readthedocs.io/en/latest/configuration.html) is set to
> `super_secret_key` in the app and should be changed by setting the env var `DOCKER_PDF_SERVER_KEY`
>
> Similarly, the default user is `admin` and can be changed by setting the env var `DOCKER_PDF_SERVER_USER`
> and the default password is `password` and can be changed by setting the env var `DOCKER_PDF_SERVER_PASSWORD`

## Ideas and Enhancements

Feature development has been driven by personal use case, primarily centered around managing a few hundred PDFs
for reading. However, I might think of additions that maintain the server's lightweight nature, such as a folder
system etc.

Feel free to contribute or raise issues to improve the Docker PDF Server!
