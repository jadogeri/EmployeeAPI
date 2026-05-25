from abc import ABC, abstractmethod
from typing import List, Optional

from sqlalchemy import Boolean

from api.dtos.employee_dto import EmployeeUpdate, EmployeeCreate
from domain.entities.employee import Employee
from models.employee_model import EmployeeModel


class IEmployeeService(ABC):
    """
    Interface defining business logic operations for Employees.
    """

    @abstractmethod
    def get_all_employees(self) -> List[Employee]:
        """Fetch all employees and map them to dictionaries."""
        pass

    @abstractmethod
    def get_employee_by_id(self, emp_id: int) -> Optional[Employee]:
        """Fetch a single employee's details by their ID."""
        pass

    @abstractmethod
    def find_employee_by_email(self, email: str) -> Optional[Employee]:
        """Find a specific employee by their name."""
        pass

    @abstractmethod
    def delete_employee_by_id(self, emp_id: int) -> Optional[bool]:
        """Find a specific employee by their name."""
        pass

    @abstractmethod
    def create_employee(self, employee: EmployeeCreate) -> Employee:
        """Create a new employee with given details."""
        pass

    @abstractmethod
    def update_employee(self, emp_id: int, employee: EmployeeUpdate) -> Employee:
        """Update an existing employee with given details."""
        pass

    @abstractmethod
    def find_active_employees(self) -> List[Employee]:
        """Fetch all active employees."""
        pass