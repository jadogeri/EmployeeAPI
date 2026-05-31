import pytest
from unittest.mock import MagicMock

# Fixed: This line was already updated correctly
from application.services.employee_service import EmployeeService

# Fixed: Removed the 'app.' prefix from all structural imports below
from domain.entities.employee import Employee
from models.employee_model import EmployeeModel
from infrastructure.repositories.interfaces.employee_repository_interface import IEmployeeRepository
from infrastructure.mappers.employee_mapper import EmployeeMapper


@pytest.fixture
def mock_repository():
    """Provides a fresh, mocked repository for each test."""
    return MagicMock(spec=IEmployeeRepository)


@pytest.fixture
def employee_service(mock_repository):
    """Provides an EmployeeService instance injected with the mock repository."""
    return EmployeeService(repository=mock_repository)


@pytest.fixture
def sample_employee_model():
    """Provides a mock EmployeeModel database object."""
    model = MagicMock(spec=EmployeeModel)
    return model


@pytest.fixture
def mock_mapper_to_entity(monkeypatch):
    """Mocks the EmployeeMapper to return a dummy Employee entity."""
    dummy_entity = MagicMock(spec=Employee)
    # Vars/dict behavior simulation
    dummy_entity.__dict__ = {"id": 1, "name": "John Doe", "email": "john@example.com"}
    
    monkeypatch.setattr(EmployeeMapper, "to_entity", lambda model: dummy_entity)
    return dummy_entity


def test_get_all_employees(employee_service, mock_repository, sample_employee_model, mock_mapper_to_entity):
    # Arrange
    mock_repository.get_all.return_value = [sample_employee_model]

    # Act
    result = employee_service.get_all_employees()

    # Assert
    assert len(result) == 1
    assert result[0]["name"] == "John Doe"
    mock_repository.get_all.assert_called_once()


def test_get_employee_by_id_found(employee_service, mock_repository, sample_employee_model, mock_mapper_to_entity):
    # Arrange
    mock_repository.get_one.return_value = sample_employee_model

    # Act
    result = employee_service.get_employee_by_id(1)

    # Assert
    assert result is not None
    assert result["id"] == 1
    mock_repository.get_one.assert_called_once_with(1)


def test_get_employee_by_id_not_found(employee_service, mock_repository):
    # Arrange
    mock_repository.get_one.return_value = None

    # Act
    result = employee_service.get_employee_by_id(999)

    # Assert
    assert result is None
    mock_repository.get_one.assert_called_once_with(999)


def test_find_employee_by_email_found(employee_service, mock_repository, sample_employee_model, mock_mapper_to_entity):
    # Arrange
    mock_repository.find_by_email.return_value = sample_employee_model

    # Act
    result = employee_service.find_employee_by_email("john@example.com")

    # Assert
    assert result is not None
    assert result["email"] == "john@example.com"
    mock_repository.find_by_email.assert_called_once_with("john@example.com")


def test_delete_employee_by_id(employee_service, mock_repository):
    # Arrange
    mock_repository.delete.return_value = True

    # Act
    result = employee_service.delete_employee_by_id(1)

    # Assert
    assert result is True
    mock_repository.delete.assert_called_once_with(1)


def test_create_employee(employee_service, mock_repository, sample_employee_model, mock_mapper_to_entity):
    # Arrange
    mock_repository.save.return_value = sample_employee_model

    # Act
    result = employee_service.create_employee(sample_employee_model)

    # Assert
    assert result is not None
    assert result["name"] == "John Doe"
    mock_repository.save.assert_called_once_with(sample_employee_model)


def test_update_employee(employee_service, mock_repository, sample_employee_model):
    # Arrange
    mock_repository.update.return_value = sample_employee_model

    # Act
    result = employee_service.update_employee(1, sample_employee_model)

    # Assert
    assert result == sample_employee_model
    mock_repository.update.assert_called_once_with(1, sample_employee_model)


def test_find_active_employees(employee_service, mock_repository, sample_employee_model, mock_mapper_to_entity):
    # Arrange
    mock_repository.get_all_active.return_value = [sample_employee_model]

    # Act
    result = employee_service.find_active_employees()

    # Assert
    assert len(result) == 1
    mock_repository.get_all_active.assert_called_once()
