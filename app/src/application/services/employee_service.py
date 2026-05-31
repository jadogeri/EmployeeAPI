from __future__ import annotations
from typing import List, Optional

from application.services.interfaces.employee_service_interface import IEmployeeService
from domain.entities.employee import Employee
from infrastructure.mappers.employee_mapper import EmployeeMapper
from infrastructure.repositories.interfaces.employee_repository_interface import (
    IEmployeeRepository,
)
from models.employee_model import EmployeeModel


class EmployeeService(IEmployeeService):
    def __init__(self, repository: IEmployeeRepository):
        self.repository = repository

    def get_all_employees(self) -> List[Employee]:
        employees: list[Employee] = []
        employee_models: list[EmployeeModel] = self.repository.get_all()
        for employee_model in employee_models:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            # Fixed: Changed __dict__() to vars() or .__dict__
            employees.append(vars(employee))
        return employees

    def get_employee_by_id(self, emp_id: int) -> Optional[Employee]:
        employee_model: EmployeeModel | None = self.repository.get_one(emp_id)
        if employee_model:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            # Fixed: Changed __dict__() to vars()
            return vars(employee)
        else:
            return None

    def find_employee_by_email(self, email: str) -> Optional[Employee]:
        employee_model: EmployeeModel | None = self.repository.find_by_email(email)
        if employee_model:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            # Fixed: Changed __dict__() to vars()
            return vars(employee)
        else:
            return None

    def delete_employee_by_id(self, emp_id: int) -> Optional[bool]:
        is_deleted: bool = self.repository.delete(emp_id)
        return is_deleted

    def create_employee(self, employee: EmployeeModel) -> Employee | None:
        employee_model: EmployeeModel = self.repository.save(employee)
        if employee_model:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            # Fixed: Changed __dict__() to vars()
            return vars(employee)
        else:
            return None

    def update_employee(
        self, emp_id: int, employee: EmployeeModel
    ) -> Optional[Employee]:  # 👈 Changed return type hint to match output structure
        """Update an existing employee with given details."""
        updated_model: EmployeeModel | None = self.repository.update(emp_id, employee)
        if updated_model:
            # Fixed: Properly map the database object back to a clean domain dictionary
            employee_entity: Employee = EmployeeMapper.to_entity(updated_model)
            return vars(employee_entity)
        return None

    def find_active_employees(self) -> List[Employee]:
        active_employees: list[Employee] = []
        all_employee_models: list[EmployeeModel] = self.repository.get_all_active()
        for employee_model in all_employee_models:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            # Fixed: Changed __dict__() to vars()
            active_employees.append(vars(employee))
        return active_employees
