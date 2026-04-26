from __future__ import annotations

from abc import ABC
from typing import List, Optional

from sqlalchemy import Boolean

from application.services.interfaces.employee_service_interface import IEmployeeService
from infrastructure.repositories.interfaces.employee_repository_interface import IEmployeeRepository
from models.employee_model import EmployeeModel


class EmployeeService(IEmployeeService):
    def __init__(self, repository: IEmployeeRepository):
        self.repository = repository

    def get_all_employees(self) -> List[dict]:
        employees = self.repository.get_all()
        return [{"id": e.id, "full_name": f"{e.first_name} {e.last_name}" , "role": e.role} for e in employees]

    def get_employee_by_id(self, emp_id: int) -> Optional[EmployeeModel]:
        employee = self.repository.get_one(emp_id)
        return employee if employee else None

    def find_employee_by_email(self, email: str) -> Optional[EmployeeModel]:
        employee = self.repository.find_by_email(email)
        return employee if employee else None


    def delete_employee_by_id(self, emp_idl: str) -> Optional[Boolean]:
        is_deleted = self.repository.delete(emp_idl)
        return is_deleted is True or is_deleted is False

    def create_employee(self, employee: EmployeeModel) -> EmployeeModel | None:
        employee = self.repository.save(employee)
        return employee if employee else None

    def update_employee(self, emp_id: str, employee: EmployeeModel) -> EmployeeModel:
        """Update an existing employee with given details."""
        pass

    def find_active_employees(self) -> List[EmployeeModel]:
        employees = self.repository.get_all_active()
        return employees












    def find_employee_by_name(self, name: str) -> Optional[dict]:
        emp = self.repository.find_by_name(name)
        return {"id": emp.id, "name": emp.name} if emp else None
