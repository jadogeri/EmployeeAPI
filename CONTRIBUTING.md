# Contributing to EmployeeAPI

Thank you for taking the time to contribute! 🎉

The following is a set of guidelines for contributing to **EmployeeAPI**. These are mostly guidelines, not hard rules — use your best judgement, and feel free to propose changes to this document via a pull request.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Submitting Pull Requests](#submitting-pull-requests)
- [Development Setup](#development-setup)
- [Style Guide](#style-guide)
- [Commit Message Convention](#commit-message-convention)

---

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## How Can I Contribute?

### Reporting Bugs

Before creating a bug report, please check existing issues to avoid duplicates.

When submitting a bug report, include:
- A clear and descriptive title
- Steps to reproduce the problem
- Expected vs. actual behavior
- Your Python version and OS
- Any relevant logs or error output

Use the **Bug Report** issue template when opening a new issue.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When suggesting an enhancement, include:
- A clear and descriptive title
- A step-by-step description of the proposed behavior
- Any alternatives you've considered
- Why this enhancement would benefit most users

Use the **Feature Request** issue template when opening a new issue.

### Submitting Pull Requests

1. **Fork** the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Set up the development environment** (see [Development Setup](#development-setup)).

3. **Make your changes** — follow the [Style Guide](#style-guide).

4. **Add or update tests** for any changed behavior.

5. **Run the test suite** and ensure all tests pass:
   ```bash
   pytest
   ```

6. **Run the linter**:
   ```bash
   flake8 .
   ```

7. **Commit your changes** following the [Commit Message Convention](#commit-message-convention).

8. **Push** to your fork and open a Pull Request against `main`.

9. Fill out the Pull Request template completely.

---

## Development Setup

```bash
# Clone your fork
git clone https://github.com/<your-username>/EmployeeAPI.git
cd EmployeeAPI/app

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install the project in editable mode with all dependencies
pip install -e .

# Run the development server
uvicorn main:app --reload
```

---

## Style Guide

- Follow [PEP 8](https://pep8.org/) for all Python code.
- Use type hints on all function signatures.
- Keep functions small and focused — one responsibility per function.
- Prefer dataclasses for domain entities and Pydantic models for API DTOs.
- Respect the clean architecture boundaries:
  - Domain layer must not import from infrastructure or application layers.
  - Application layer must depend only on domain entities and repository/service interfaces.
  - Infrastructure layer implements the interfaces defined in the application layer.

---

## Commit Message Convention

Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <short summary>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
```
feat(employees): add pagination to GET /employees endpoint
fix(mapper): handle null role field in employee_mapper
docs(readme): update installation instructions
test(repository): add unit tests for find_by_name
```
