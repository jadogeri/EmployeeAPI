from typing import List, Optional

from app.src.models.employee_model import EmployeeModel
from application.controllers.interfaces.employee_controller_interface import (
    IEmployeeController,
)
from application.services.interfaces.employee_service_interface import IEmployeeService
from domain.entities.employee import Employee
from api.dtos.employee_dto import EmployeeCreate, EmployeeUpdate


class EmployeeController(IEmployeeController):
    def __init__(self, service: IEmployeeService):
        self.service = service

    def get_all_employees(self) -> List[Employee]:
        return self.service.get_all_employees()

    def get_employee_by_id(self, emp_id: int) -> Optional[Employee]:
        return self.service.get_employee_by_id(emp_id)

    def find_employee_by_email(self, email: str) -> Optional[Employee]:
        return self.service.find_employee_by_email(email)

    def delete_employee_by_id(self, emp_id: int) -> bool | None:
        return self.service.delete_employee_by_id(emp_id)

    def create_employee(self, employee: EmployeeCreate) -> Employee:
        return self.service.create_employee(employee)


    def update_employee(self, emp_id: int, employee: EmployeeUpdate) -> Optional[Employee]:
        # 👈 Fixed: Convert incoming update Pydantic schema to SQLAlchemy model
        employee_model = EmployeeModel(
            name=employee.name,
            email=employee.email,
            is_active=getattr(employee, 'is_active', True)
        )
        return self.service.update_employee(emp_id, employee_model)

    def find_active_employees(self) -> List[Employee]:
        return self.service.find_active_employees()
