"""
Employee Repository Module
------------------------
Description: Concrete implementation of BaseRepository for handling
             Employee entity persistence logic.

Author: Joseph Adogeri
Version: 1.0.0
Since: 2024-05-20
File: employee_repository.py
License: MIT
"""
from __future__ import annotations

from infrastructure.repositories.interfaces.employee_repository_interface import IEmployeeRepository
from models.employee_model import EmployeeModel

class EmployeeRepository(IEmployeeRepository):
    def __init__(self):
        """
        Initializes the EmployeeRepository with the Employee model.
        """
        super().__init__(EmployeeModel)

    def find_by_name(self, name: str) -> EmployeeModel | None:
        """
        Uses the inherited self.query property from BaseRepository.
        """
        return self.query.filter_by(name=name).first()

    def get_by_roles(self) -> list[EmployeeModel]:
        """
        Uses the inherited self.query property to filter active records.
        """
        return self.query.filter_by(is_active=True).all()
