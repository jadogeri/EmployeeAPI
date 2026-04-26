from __future__ import annotations

from abc import ABC
from typing import List, Optional

from application.services.interfaces.employee_service_interface import IEmployeeService
from infrastructure.repositories.interfaces.employee_repository_interface import IEmployeeRepository


class EmployeeService(IEmployeeService, ABC):
    def __init__(self, repository: IEmployeeRepository):
        self.repository = repository

    def get_all_employees(self) -> List[dict]:
        employees = self.repository.get_all()
        return [{"id": e.id, "full_name": f"{e.first_name} {e.last_name}" , "role": e.role} for e in employees]

    def get_employee_details(self, emp_id: int) -> Optional[dict]:
        emp = self.repository.get_one(emp_id)
        if not emp:
            return None
        return {"id": emp.id, "name": emp.name, "role": emp.role}

    def find_employee_by_name(self, name: str) -> Optional[dict]:
        emp = self.repository.find_by_name(name)
        return {"id": emp.id, "name": emp.name} if emp else None
