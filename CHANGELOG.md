## [1.6.1](https://github.com/homelabdude/docker-pdf-server/compare/v1.6.0...v1.6.1) (2026-06-03)
# [1.7.0-beta.2](https://github.com/homelabdude/docker-pdf-server/compare/v1.7.0-beta.1...v1.7.0-beta.2) (2026-07-17)


### Bug Fixes

* A fix to solve auth issues if you are running behind a proxy ([855ab6d](https://github.com/homelabdude/docker-pdf-server/commit/855ab6d84ef9a3d9d3852b0c8db5b9e3f2f76b9f))
* Login broken when running behind a reverse proxy ([b2d9d8c](https://github.com/homelabdude/docker-pdf-server/commit/b2d9d8c2a188411b101459a0fea89c7b97b92136))

# [1.7.0-beta.1](https://github.com/homelabdude/docker-pdf-server/compare/v1.6.0...v1.7.0-beta.1) (2026-05-31)


### Bug Fixes

* bump typing-extensions from 4.12.2 to 4.15.0 ([#70](https://github.com/homelabdude/docker-pdf-server/issues/70)) ([32700eb](https://github.com/homelabdude/docker-pdf-server/commit/32700ebb87ca3dd9f0ed0bbd968cd97475493c6d))
* Fix Dockerfile ([#78](https://github.com/homelabdude/docker-pdf-server/issues/78)) ([5a8f443](https://github.com/homelabdude/docker-pdf-server/commit/5a8f4434f77f8ea53a74614d3c6de0a60955c3df))
* implement ProxyFix to trust the X-Forwarded-Host/X-Forwarded-Proto headers from proxy ([95ae3a3](https://github.com/homelabdude/docker-pdf-server/commit/95ae3a3e4d60b88a701517a65fc7a71d507a4aad))
* perfomance fix to massively reduce the size of the generated thumbnails ([97668a2](https://github.com/homelabdude/docker-pdf-server/commit/97668a2e3dfd298bd70b8247a8d1aad8dc696555))
* Update README and add delete user button ([#79](https://github.com/homelabdude/docker-pdf-server/issues/79)) ([3fe0b6f](https://github.com/homelabdude/docker-pdf-server/commit/3fe0b6f97d1d6cf40c236e3274e228b983eabd12))
* Update to correct URL in semver metadata ([#77](https://github.com/homelabdude/docker-pdf-server/issues/77)) ([aa632f3](https://github.com/homelabdude/docker-pdf-server/commit/aa632f37f21dd6f93dbbbf71b8fe43f0f2e30360))


### Features

* Adding EPUB support ([9cd4ab0](https://github.com/homelabdude/docker-pdf-server/commit/9cd4ab098f6e11fee601eb280fb2d992028eaf3c))
* Rewrite to ([#76](https://github.com/homelabdude/docker-pdf-server/issues/76)) ([90ee085](https://github.com/homelabdude/docker-pdf-server/commit/90ee0858e7ab79ae6e48cba829dbaecda1f37b33))
* update dependencies in beta ([c2c7408](https://github.com/homelabdude/docker-pdf-server/commit/c2c74084218ffa2b2582e68a873af095a17d71c8))
* version bumps on Jinja, Markupsafe and SQLAlchemy ([59c381c](https://github.com/homelabdude/docker-pdf-server/commit/59c381c9216d9c7111f96228a0a02356ab13a229))

# [1.6.0-beta.4](https://github.com/homelabdude/docker-pdf-server/compare/v1.6.0-beta.3...v1.6.0-beta.4) (2026-05-31)


### Bug Fixes

* implement ProxyFix to trust the X-Forwarded-Host/X-Forwarded-Proto headers from proxy ([95ae3a3](https://github.com/homelabdude/docker-pdf-server/commit/95ae3a3e4d60b88a701517a65fc7a71d507a4aad))
# [1.6.0](https://github.com/homelabdude/docker-pdf-server/compare/v1.5.0...v1.6.0) (2026-05-31)


### Features

* Add workflow_dispatch trigger to CI workflow ([308c20c](https://github.com/homelabdude/docker-pdf-server/commit/308c20c7494e5065759277cefe553e66c98070fb))
* Version updates and release to add EPUB support + optimised thumbnail generation ([#94](https://github.com/homelabdude/docker-pdf-server/issues/94)) ([ae42e56](https://github.com/homelabdude/docker-pdf-server/commit/ae42e56ae0552d646988dea655b9b828728fb594))

# [1.6.0-beta.3](https://github.com/homelabdude/docker-pdf-server/compare/v1.6.0-beta.2...v1.6.0-beta.3) (2026-05-31)


### Bug Fixes

* perfomance fix to massively reduce the size of the generated thumbnails ([97668a2](https://github.com/homelabdude/docker-pdf-server/commit/97668a2e3dfd298bd70b8247a8d1aad8dc696555))

# [1.6.0-beta.2](https://github.com/homelabdude/docker-pdf-server/compare/v1.6.0-beta.1...v1.6.0-beta.2) (2026-05-14)


### Features

* Adding EPUB support ([9cd4ab0](https://github.com/homelabdude/docker-pdf-server/commit/9cd4ab098f6e11fee601eb280fb2d992028eaf3c))

# [1.6.0-beta.1](https://github.com/homelabdude/docker-pdf-server/compare/v1.5.0...v1.6.0-beta.1) (2026-05-13)


### Bug Fixes

* bump typing-extensions from 4.12.2 to 4.15.0 ([#70](https://github.com/homelabdude/docker-pdf-server/issues/70)) ([32700eb](https://github.com/homelabdude/docker-pdf-server/commit/32700ebb87ca3dd9f0ed0bbd968cd97475493c6d))
* Fix Dockerfile ([#78](https://github.com/homelabdude/docker-pdf-server/issues/78)) ([5a8f443](https://github.com/homelabdude/docker-pdf-server/commit/5a8f4434f77f8ea53a74614d3c6de0a60955c3df))
* Update README and add delete user button ([#79](https://github.com/homelabdude/docker-pdf-server/issues/79)) ([3fe0b6f](https://github.com/homelabdude/docker-pdf-server/commit/3fe0b6f97d1d6cf40c236e3274e228b983eabd12))
* Update to correct URL in semver metadata ([#77](https://github.com/homelabdude/docker-pdf-server/issues/77)) ([aa632f3](https://github.com/homelabdude/docker-pdf-server/commit/aa632f37f21dd6f93dbbbf71b8fe43f0f2e30360))


### Features

* Rewrite to ([#76](https://github.com/homelabdude/docker-pdf-server/issues/76)) ([90ee085](https://github.com/homelabdude/docker-pdf-server/commit/90ee0858e7ab79ae6e48cba829dbaecda1f37b33))
* update dependencies in beta ([c2c7408](https://github.com/homelabdude/docker-pdf-server/commit/c2c74084218ffa2b2582e68a873af095a17d71c8))
* version bumps on Jinja, Markupsafe and SQLAlchemy ([59c381c](https://github.com/homelabdude/docker-pdf-server/commit/59c381c9216d9c7111f96228a0a02356ab13a229))

# [1.5.0](https://github.com/homelabdude/docker-pdf-server/compare/v1.4.1...v1.5.0) (2026-05-12)


### Features

* A pretty major rewrite after quite sometime but breaks nothing and should just work with your existing library and logins ([#81](https://github.com/homelabdude/docker-pdf-server/issues/81)) ([9d80280](https://github.com/homelabdude/docker-pdf-server/commit/9d8028082bf07663b41a6c0d426fffee36990838))
* Update README.md with new repository links ([cc7d096](https://github.com/homelabdude/docker-pdf-server/commit/cc7d09697c8314b7b8ff9f93b0aa3508138a2cd8))
* version bumps on Jinja, Markupsafe and SQLAlchemy ([#51](https://github.com/homelabdude/docker-pdf-server/issues/51)) ([829533f](https://github.com/homelabdude/docker-pdf-server/commit/829533fb45cc95ab8bf3621a4fd794a24b48b75c))

# [1.5.0-beta.6](https://github.com/homelabdude/docker-pdf-server/compare/v1.5.0-beta.5...v1.5.0-beta.6) (2026-05-12)


### Features

* version bumps on Jinja, Markupsafe and SQLAlchemy ([#51](https://github.com/homelabdude/docker-pdf-server/issues/51)) ([829533f](https://github.com/homelabdude/docker-pdf-server/commit/829533fb45cc95ab8bf3621a4fd794a24b48b75c))

# [1.5.0-beta.5](https://github.com/homelabdude/docker-pdf-server/compare/v1.5.0-beta.4...v1.5.0-beta.5) (2026-05-12)


### Bug Fixes

* Update README and add delete user button ([#79](https://github.com/homelabdude/docker-pdf-server/issues/79)) ([3fe0b6f](https://github.com/homelabdude/docker-pdf-server/commit/3fe0b6f97d1d6cf40c236e3274e228b983eabd12))

# [1.5.0-beta.4](https://github.com/homelabdude/docker-pdf-server/compare/v1.5.0-beta.3...v1.5.0-beta.4) (2026-05-12)


### Bug Fixes

* Fix Dockerfile ([#78](https://github.com/homelabdude/docker-pdf-server/issues/78)) ([5a8f443](https://github.com/homelabdude/docker-pdf-server/commit/5a8f4434f77f8ea53a74614d3c6de0a60955c3df))

# [1.5.0-beta.3](https://github.com/homelabdude/docker-pdf-server/compare/v1.5.0-beta.2...v1.5.0-beta.3) (2026-05-12)


### Bug Fixes

* Update to correct URL in semver metadata ([#77](https://github.com/homelabdude/docker-pdf-server/issues/77)) ([aa632f3](https://github.com/homelabdude/docker-pdf-server/commit/aa632f37f21dd6f93dbbbf71b8fe43f0f2e30360))


### Features

* Rewrite to ([#76](https://github.com/homelabdude/docker-pdf-server/issues/76)) ([90ee085](https://github.com/homelabdude/docker-pdf-server/commit/90ee0858e7ab79ae6e48cba829dbaecda1f37b33))

# [1.5.0-beta.2](https://github.com/ash0ne/docker-pdf-server/compare/v1.5.0-beta.1...v1.5.0-beta.2) (2025-06-18)


### Features

* update dependencies in beta ([c2c7408](https://github.com/ash0ne/docker-pdf-server/commit/c2c74084218ffa2b2582e68a873af095a17d71c8))

# [1.5.0-beta.1](https://github.com/ash0ne/docker-pdf-server/compare/v1.4.1...v1.5.0-beta.1) (2025-01-19)


### Features

* version bumps on Jinja, Markupsafe and SQLAlchemy ([59c381c](https://github.com/ash0ne/docker-pdf-server/commit/59c381c9216d9c7111f96228a0a02356ab13a229))

## [1.4.1](https://github.com/ash0ne/docker-pdf-server/compare/v1.4.0...v1.4.1) (2024-11-30)


### Bug Fixes

* version bumps  ([527111b](https://github.com/ash0ne/docker-pdf-server/commit/527111b85d798f7d1c8738df1cdb817caae1e2aa))

# [1.4.0](https://github.com/ash0ne/docker-pdf-server/compare/v1.3.0...v1.4.0) (2024-10-01)


### Features

* Adding user management, RBAC and guest access. ([fc63cc6](https://github.com/ash0ne/docker-pdf-server/commit/fc63cc6b8525bf5fc154fe5d49b5d9fbe89f4da6))
* adding volume deets to the sample command ([617aea0](https://github.com/ash0ne/docker-pdf-server/commit/617aea05e84cdd26f863c816d666bd50892deff0))
* User management and Guest Access ([d95515a](https://github.com/ash0ne/docker-pdf-server/commit/d95515a74a7fed0802ae28859dd44bb14bb53a3d))
* users and rbac ([1ebd5e5](https://github.com/ash0ne/docker-pdf-server/commit/1ebd5e5b898e7bca164e2812460b2d67fd0a8642))

# [1.4.0-beta.3](https://github.com/ash0ne/docker-pdf-server/compare/v1.4.0-beta.2...v1.4.0-beta.3) (2024-09-09)


### Features

* adding volume deets to the sample command ([617aea0](https://github.com/ash0ne/docker-pdf-server/commit/617aea05e84cdd26f863c816d666bd50892deff0))

# [1.4.0-beta.2](https://github.com/ash0ne/docker-pdf-server/compare/v1.4.0-beta.1...v1.4.0-beta.2) (2024-09-09)


### Features

* users and rbac ([1ebd5e5](https://github.com/ash0ne/docker-pdf-server/commit/1ebd5e5b898e7bca164e2812460b2d67fd0a8642))

# [1.4.0-beta.1](https://github.com/ash0ne/docker-pdf-server/compare/v1.3.0...v1.4.0-beta.1) (2024-06-22)


### Features

* Adding user management, RBAC and guest access. ([fc63cc6](https://github.com/ash0ne/docker-pdf-server/commit/fc63cc6b8525bf5fc154fe5d49b5d9fbe89f4da6))
* User management and Guest Access ([d95515a](https://github.com/ash0ne/docker-pdf-server/commit/d95515a74a7fed0802ae28859dd44bb14bb53a3d))

# [1.3.0](https://github.com/ash0ne/docker-pdf-server/compare/v1.2.0...v1.3.0) (2024-04-08)


### Features

* Adding ARM builds ([e25dd5e](https://github.com/ash0ne/docker-pdf-server/commit/e25dd5efaf16b92df6e30fd890cd31e28a4d3929))
* Adding ARM images ([1d95dd8](https://github.com/ash0ne/docker-pdf-server/commit/1d95dd8951928dce5f7f75945f9ea1d409199d07))

# [1.3.0-beta.2](https://github.com/ash0ne/docker-pdf-server/compare/v1.3.0-beta.1...v1.3.0-beta.2) (2024-04-08)


### Features

* Adding ARM images ([1d95dd8](https://github.com/ash0ne/docker-pdf-server/commit/1d95dd8951928dce5f7f75945f9ea1d409199d07))

# [1.3.0-beta.1](https://github.com/ash0ne/docker-pdf-server/compare/v1.2.0...v1.3.0-beta.1) (2024-04-08)


### Features

* Adding ARM builds ([e25dd5e](https://github.com/ash0ne/docker-pdf-server/commit/e25dd5efaf16b92df6e30fd890cd31e28a4d3929))

# [1.2.0](https://github.com/ash0ne/docker-pdf-server/compare/v1.1.0...v1.2.0) (2024-04-07)


### Bug Fixes

* adding github plugin to sem ver ([a3dd5ad](https://github.com/ash0ne/docker-pdf-server/commit/a3dd5adf6d24956cc65c7c5eb336d1558f4e375a))
* minor fix to the CI to install all dependencies of semantic release ([bf998ef](https://github.com/ash0ne/docker-pdf-server/commit/bf998ef32cd205b6f4b766a00851c1137e4d9d6e))


### Features

* Updating CI to publish to Docker ([66e6671](https://github.com/ash0ne/docker-pdf-server/commit/66e6671c37b6c99d2560b6ee4354234e7bd6146b))

# [1.2.0-beta.1](https://github.com/ash0ne/docker-pdf-server/compare/v1.1.0...v1.2.0-beta.1) (2024-04-07)


### Bug Fixes

* adding github plugin to sem ver ([a3dd5ad](https://github.com/ash0ne/docker-pdf-server/commit/a3dd5adf6d24956cc65c7c5eb336d1558f4e375a))
* minor fix to the CI to install all dependencies of semantic release ([bf998ef](https://github.com/ash0ne/docker-pdf-server/commit/bf998ef32cd205b6f4b766a00851c1137e4d9d6e))


### Features

* Updating CI to publish to Docker ([66e6671](https://github.com/ash0ne/docker-pdf-server/commit/66e6671c37b6c99d2560b6ee4354234e7bd6146b))

# [1.1.0-beta.2](https://github.com/ash0ne/docker-pdf-server/compare/v1.1.0-beta.1...v1.1.0-beta.2) (2024-04-07)


### Bug Fixes

* adding github plugin to sem ver ([a3dd5ad](https://github.com/ash0ne/docker-pdf-server/commit/a3dd5adf6d24956cc65c7c5eb336d1558f4e375a))
* adding in npm to update package.json ([4efe418](https://github.com/ash0ne/docker-pdf-server/commit/4efe418763c93eb522480e0e5f66e0cc87b36cb7))
* minor fix to the CI to install all dependencies of semantic release ([bf998ef](https://github.com/ash0ne/docker-pdf-server/commit/bf998ef32cd205b6f4b766a00851c1137e4d9d6e))
* plugin config ([32c4e40](https://github.com/ash0ne/docker-pdf-server/commit/32c4e400544b52cb5c4827d2a5029a1f2afd4492))


### Features

* Updating CI to publish to Docker ([66e6671](https://github.com/ash0ne/docker-pdf-server/commit/66e6671c37b6c99d2560b6ee4354234e7bd6146b))

# [1.1.0-beta.2](https://github.com/ash0ne/docker-pdf-server/compare/v1.1.0-beta.1...v1.1.0-beta.2) (2024-04-07)


### Bug Fixes

* adding github plugin to sem ver ([a3dd5ad](https://github.com/ash0ne/docker-pdf-server/commit/a3dd5adf6d24956cc65c7c5eb336d1558f4e375a))
* adding in npm to update package.json ([4efe418](https://github.com/ash0ne/docker-pdf-server/commit/4efe418763c93eb522480e0e5f66e0cc87b36cb7))
* plugin config ([32c4e40](https://github.com/ash0ne/docker-pdf-server/commit/32c4e400544b52cb5c4827d2a5029a1f2afd4492))


### Features

* Updating CI to publish to Docker ([66e6671](https://github.com/ash0ne/docker-pdf-server/commit/66e6671c37b6c99d2560b6ee4354234e7bd6146b))

# [1.1.0-beta.1](https://github.com/ash0ne/docker-pdf-server/compare/v1.0.0...v1.1.0-beta.1) (2024-04-07)


### Bug Fixes

* fixing semantic-release steps ([fc7afb5](https://github.com/ash0ne/docker-pdf-server/commit/fc7afb533193d4a37bb5d5c0dafcfce8738ee04c))
* remove redundant GitLab plugins ([aa72cd2](https://github.com/ash0ne/docker-pdf-server/commit/aa72cd284509c51156a2ba64db5120a19f29b780))
* updating the ci to release beta and add change logs ([bf118a5](https://github.com/ash0ne/docker-pdf-server/commit/bf118a5a0734c5c70a5eac48f705f130e81dc351))
* Updating the ci to release beta versions and add change logs ([c2e51bd](https://github.com/ash0ne/docker-pdf-server/commit/c2e51bd0f20f07bd2b13448eec85242f04bcc02d))


### Features

* CI updates to support pre-release image publishing. ([eec63a4](https://github.com/ash0ne/docker-pdf-server/commit/eec63a4bceed1c74c386fb42ed66f75ae541db54))
