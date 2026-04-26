from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy import Boolean

from models.employee_model import EmployeeModel


class IEmployeeService(ABC):
    """
    Interface defining business logic operations for Employees.
    """

    @abstractmethod
    def get_all_employees(self) -> List[EmployeeModel]:
        """Fetch all employees and map them to dictionaries."""
        pass

    @abstractmethod
    def get_employee_by_id(self, emp_id: int) -> Optional[EmployeeModel]:
        """Fetch a single employee's details by their ID."""
        pass

    @abstractmethod
    def find_employee_by_email(self, email: str) -> Optional[EmployeeModel]:
        """Find a specific employee by their name."""
        pass

    @abstractmethod
    def delete_employee_by_id(self, emp_idl: str) -> Optional[Boolean]:
        """Find a specific employee by their name."""
        pass

    @abstractmethod
    def create_employee(self, employee: EmployeeModel) -> EmployeeModel:
        """Create a new employee with given details."""
        pass

    @abstractmethod
    def update_employee(self, emp_id: str, employee: EmployeeModel) -> EmployeeModel:
        """Update an existing employee with given details."""
        pass

    @abstractmethod
    def find_active_employees(self) -> List[EmployeeModel]:
        """Fetch all active employees."""
        pass