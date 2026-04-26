from abc import ABC, abstractmethod
from typing import List, Optional

from infrastructure.repositories.interfaces.base_repository import BaseRepository
from models.employee_model import EmployeeModel

class IEmployeeRepository(BaseRepository[EmployeeModel], ABC):
    """
    Interface for Employee Repository.
    Inherits generic CRUD logic from BaseRepository and enforces custom methods.
    """

    @abstractmethod
    def find_by_name(self, name: str) -> Optional[EmployeeModel]:
        """Specific query to find an employee by name."""
        pass

    @abstractmethod
    def get_by_roles(self) -> List[EmployeeModel]:
        """Specific query to find active employees by roles."""
        pass
