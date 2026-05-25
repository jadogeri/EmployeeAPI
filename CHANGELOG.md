# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- PostgreSQL integration via `asyncpg`
- OAuth2 / JWT authentication on write endpoints
- Pagination and filtering on `GET /employees`
- Docker + docker-compose setup

---

## [1.0.0] - 2026-05-25

### Added
- Initial FastAPI application scaffold (`main.py`)
- `Employee` domain entity as a Python dataclass
- `EmployeeModel` SQLAlchemy ORM model with UUID primary key, `first_name`, `last_name`, `email`, `role`, `is_active` fields
- Pydantic DTOs: `EmployeeBase`, `EmployeeCreate`, `EmployeeRead`
- `IEmployeeRepository` and `IEmployeeService` abstract interfaces
- `EmployeeRepository` concrete implementation with `find_by_name` query
- `EmployeeService` application-layer business logic
- `employee_mapper.py` for clean Model ↔ Entity translation
- Flask-SQLAlchemy `db` singleton with `DeclarativeBase`
- `pyproject.toml` modern project configuration with all dependencies
- `commands.txt` CLI command reference
- `test_main.http` REST Client test file
- GitHub Actions CI workflow (`python-app.yml`) running Pytest and Flake8

---

[Unreleased]: https://github.com/jadogeri/EmployeeAPI/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/jadogeri/EmployeeAPI/releases/tag/v1.0.0
