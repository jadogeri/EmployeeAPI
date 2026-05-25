# 🧑‍💼 FastAPI Employee CRUD API

**Author:** Joseph Adogeri
<br/>
**Version:** 1.0
<br/>
**Date:** May 25, 2026

<div align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="400">
</div>

---

## Description

A high-performance Python FastAPI CRUD (Create, Read, Update, Delete) API for managing employee information. This project features automatic Pydantic data validation, clean architecture layering (Domain → Application → Infrastructure), and SQLAlchemy ORM persistence.

---

## 📍 Table of Contents

*   [🛠 Tech Stack](#-tech-stack)
*   [📦 Installation & Setup](#-installation--setup)
*   [📖 API Documentation](#-api-documentation-swagger)
*   [🛣 API Endpoints](#-api-endpoints)
*   [🧪 Testing with REST Client](#-testing-with-rest-client)
*   [🧠 Post-Mortem: Challenges & Learning](#-post-mortem-challenges--learning)
*   [🚀 Future Roadmap](#-future-roadmap-scaling-the-project)
*   [📄 Project Structure](#-project-structure)
*   [📄 License](#-license)

---

## 🛠 Tech Stack

*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Validation:** [Pydantic](https://pydantic.dev)
*   **Server:** [Uvicorn](https://uvicorn.org)
*   **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) via Flask-SQLAlchemy
*   **Package Manager:** Pip (via `pyproject.toml`)
*   **Architecture:** Clean Architecture (Domain / Application / Infrastructure)
*   **CI/CD:** GitHub Actions (Automated Pytest & Flake8)
*   **API Documentation:** Interactive Swagger UI & ReDoc (Built-in)

---

## 📦 Installation & Setup
Note: Command references are available in `commands.txt`

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jadogeri/EmployeeAPI.git
    cd EmployeeAPI/app
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install project & dependencies:**
    ```bash
    pip install -e .
    ```

4.  **Run the application:**
    ```bash
    # Using standard uvicorn
    uvicorn main:app --reload
    ```

---

## 📖 API Documentation (Swagger)

Once the server is running, access the interactive documentation at:

*   **Swagger UI:** `http://localhost:8000/docs`
*   **ReDoc:** `http://localhost:8000/redoc`

---

## 🛣 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| 📥 **GET** | `/employees` | **Get All:** Retrieve a list of all employees |
| 🔍 **GET** | `/employees/{id}` | **Get One:** Retrieve details for a specific employee by ID |
| ✨ **POST** | `/employees` | **Create:** Add a new employee with JSON payload |
| 🔄 **PUT** | `/employees/{id}` | **Update:** Modify existing employee information |
| 🗑️ **DELETE** | `/employees/{id}` | **Delete:** Remove an employee from the system |

---

## 🧪 Testing with REST Client

You can test the API endpoints using the `test_main.http` file. If you are using VS Code, install the **REST Client** extension to run these requests directly.

---

## 🧠 Post-Mortem: Challenges & Learning

### 🛠 Key Challenges & Solutions

*   **Clean Architecture Layering:** Keeping domain logic strictly separated from infrastructure concerns (SQLAlchemy models, database sessions) required careful interface design.
    *   *Solution:* Introduced `IEmployeeRepository` and `IEmployeeService` interfaces so that higher layers depend on abstractions, not concretions.
*   **ORM & Domain Entity Mapping:** Translating between the `EmployeeModel` (SQLAlchemy) and the `Employee` dataclass (domain) without leaking persistence logic into business rules.
    *   *Solution:* Dedicated `employee_mapper.py` encapsulates all mapping logic, keeping both layers clean.
*   **UUID Primary Keys:** Generating and validating UUID-based string IDs consistently across create and read paths.
    *   *Solution:* UUID generation is handled at the service layer before persistence, ensuring the domain always owns the identity.

### 🎓 Lessons Learned

*   **Clean Architecture in Python:** Gained a deep understanding of layering Domain → Application → Infrastructure and how dependency inversion enables testability.
*   **Pydantic v2 DTOs:** Mastered field-level validation with `EmailStr`, `Field` constraints, and `model_config` for ORM compatibility.
*   **FastAPI Dependency Injection:** Learned to wire services and repositories through FastAPI's `Depends` system for clean, testable route handlers.

---

## 🚀 Future Roadmap: Scaling the Project

1.  **PostgreSQL Integration:** Replace the default SQLite setup with **PostgreSQL** for production-grade persistence and concurrent access.
2.  **Authentication & Authorization:** Implement **OAuth2 with JWT tokens** to secure `POST`, `PUT`, and `DELETE` endpoints with role-based access control.
3.  **Containerization:** Add a `Dockerfile` and `docker-compose.yml` for consistent deployment across environments.
4.  **Async Database Drivers:** Migrate to `asyncpg` + `SQLAlchemy async` to leverage FastAPI's full async capabilities under load.
5.  **Pagination & Filtering:** Add query-parameter-based pagination and filtering to the `GET /employees` endpoint for large datasets.

---

## 📄 Project Structure

```text
📂 EmployeeAPI/ (Root)
├── 📂 .github/
│   ├── 📂 workflows/
│   │   └── 📄 python-app.yml       # 🤖 GitHub Actions CI Configuration
│   ├── 📂 ISSUE_TEMPLATE/
│   │   ├── 📄 bug_report.md
│   │   └── 📄 feature_request.md
│   └── 📄 PULL_REQUEST_TEMPLATE.md
├── 📂 app/
│   ├── 📄 main.py                  # 🚀 FastAPI entry point
│   ├── 📄 pyproject.toml           # 📦 Modern project configuration
│   ├── 📄 commands.txt             # ⌨️ CLI Command reference
│   ├── 📄 test_main.http           # ⚡ REST Client test file
│   └── 📂 src/
│       ├── 📂 api/dtos/
│       │   └── 📄 employee_dto.py  # 📋 Pydantic request/response schemas
│       ├── 📂 application/
│       │   ├── 📂 controllers/     # 🎮 Route controllers
│       │   └── 📂 services/        # ⚙️ Business logic & service interfaces
│       ├── 📂 domain/entities/
│       │   └── 📄 employee.py      # 🏛️ Core domain entity (dataclass)
│       ├── 📂 infrastructure/
│       │   ├── 📄 database.py      # 🗄️ SQLAlchemy DB setup
│       │   ├── 📂 mappers/         # 🔄 Model ↔ Entity mappers
│       │   └── 📂 repositories/    # 📚 Data access + interfaces
│       └── 📂 models/
│           └── 📄 employee_model.py # 🗃️ SQLAlchemy ORM model
├── 📄 README.md                    # 📖 Project documentation
├── 📄 CHANGELOG.md                 # 📝 Version history
├── 📄 CONTRIBUTING.md              # 🤝 Contribution guidelines
├── 📄 LICENSE                      # ⚖️ MIT License
└── 📄 CODE_OF_CONDUCT.md           # 📜 Community standards
```

---

## 📄 License

[MIT License](./LICENSE)
