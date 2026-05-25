from __future__ import annotations
from typing import List, Optional

from application.services.interfaces.employee_service_interface import IEmployeeService
from domain.entities.employee import Employee
from infrastructure.mappers.employee_mapper import EmployeeMapper
from infrastructure.repositories.interfaces.employee_repository_interface import IEmployeeRepository
from models.employee_model import EmployeeModel


class EmployeeService(IEmployeeService):
    def __init__(self, repository: IEmployeeRepository):
        self.repository = repository

    def get_all_employees(self) -> List[Employee]:
        employees: list[Employee] = []
        employee_models: list[EmployeeModel] = self.repository.get_all()
        for employee_model in employee_models:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            employees.append(employee.__dict__())
        return employees

    def get_employee_by_id(self, emp_id: int) -> Optional[Employee]:
        employee_model : EmployeeModel | None = self.repository.get_one(emp_id)
        if employee_model:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            return employee.__dict__()
        else:
            return  None

    def find_employee_by_email(self, email: str) -> Optional[Employee]:
        employee_model : EmployeeModel | None = self.repository.find_by_email(email)
        if employee_model:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            return employee.__dict__()
        else:
            return  None

    def delete_employee_by_id(self, emp_id: int) -> Optional[bool]:
        is_deleted : bool = self.repository.delete(emp_idl)
        return is_deleted if is_deleted or not is_deleted else None

    def create_employee(self, employee: EmployeeModel) -> Employee | None:
        employee_model : EmployeeModel= self.repository.save(employee)
        if employee_model:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            return employee.__dict__()
        else:
            return  None

    def update_employee(self, emp_id: int, employee: EmployeeModel) -> EmployeeModel:
        """Update an existing employee with given details."""
        pass

    def find_active_employees(self) -> List[Employee]:
        active_employees: list[Employee] = []
        all_employee_models : list[EmployeeModel]= self.repository.get_all_active()
        for employee_model in all_employee_models:
            employee: Employee = EmployeeMapper.to_entity(employee_model)
            active_employees.append(employee.__dict__())
        return active_employees





