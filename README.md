[![Mypy](https://github.com/NiklasvonM/python-boilerplate/actions/workflows/mypy.yml/badge.svg)](https://github.com/NiklasvonM/python-boilerplate/actions/workflows/mypy.yml)
[![Ruff](https://github.com/NiklasvonM/python-boilerplate/actions/workflows/ruff.yml/badge.svg)](https://github.com/NiklasvonM/python-boilerplate/actions/workflows/ruff.yml)
[![Tests](https://github.com/NiklasvonM/python-boilerplate/actions/workflows/tests.yml/badge.svg)](https://github.com/NiklasvonM/python-boilerplate/actions/workflows/tests.yml)
[![Security](https://github.com/NiklasvonM/python-boilerplate/actions/workflows/bandit.yml/badge.svg)](https://github.com/NiklasvonM/python-boilerplate/actions/workflows/bandit.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Python Boilerplate

This repository serves as a comprehensive toolkit and boilerplate for initiating Python projects, embedding a selection of configurations and tools tailored to streamline development workflows. It integrates industry-standard practices and personal preferences to offer a solid foundation for building robust Python applications.

Most of the tools used should work with Python >= 3.8. However, the logging requires Python >= 3.12.

## Tools

- [Poetry](https://python-poetry.org/) as the build tools instead of pip
- CI Pipeline for GitHub including:
  - [Ruff](https://github.com/astral-sh/ruff): fast linter and formatter, replacing [Pylint](https://github.com/pylint-dev/pylint)/[Flake8](https://github.com/PyCQA/flake8) and [Black](https://github.com/psf/black)
  - [Pytest](https://github.com/pytest-dev/pytest): unit tests
  - [Mypy](https://github.com/python/mypy): static type checker
  - [Bandit](https://github.com/PyCQA/bandit): security
- [Docker](https://www.docker.com/) and docker-compose: Simplify deployment and ensure consistency across environments with Docker, including a .dockerignore file for Docker-specific exclusions.
- [Uvicorn](https://github.com/encode/uvicorn)/[FastAPI](https://github.com/tiangolo/fastapi) server
- [Prometheus](https://github.com/prometheus/prometheus): monitoring An open-source monitoring system with a dimensional data model, flexible query language, efficient time series database, and modern alerting approach. Prometheus
- Custom jsonl Logging: Configure logging to use JSON lines format for easier parsing and processing of log data, taken from [James Murphy](https://github.com/mCodingLLC/VideosSampleCode/tree/master/videos/135_modern_logging).
- VSCode configurations
- Changelog
- .gitignore: standard Python gitignore
- GitHub badges

## Usage

This boilerplate is structured to be downloaded and adapted according to the specific needs of your project. Given its tailored nature, you may find certain components more relevant than others. It is designed with the flexibility to easily remove or replace elements, depending on the project requirements.

## Note

While this boilerplate is crafted with personal preferences and experiences in mind, it is open for adaptation and contributions. The intention is to provide a starting point that can be customized to fit a variety of Python projects, promoting best practices and efficient development processes.
