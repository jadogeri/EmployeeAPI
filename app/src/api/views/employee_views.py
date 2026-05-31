from fastapi import APIRouter, Depends, status, HTTPException
from fastapi_restful.cbv import cbv  # You will need to: pip install fastapi-restful
from dependency_injector.wiring import inject, Provide
from typing import List

from application.controllers.interfaces.employee_controller_interface import (
    IEmployeeController,
)
from api.dtos.employee_dto import EmployeeCreate, EmployeeUpdate, EmployeeRead
from container import Container

router = APIRouter(prefix="/employees", tags=["Employees"])


@cbv(router)  # Use cbv instead of View
class EmployeeView:
    @inject
    def __init__(
        self,
        controller: IEmployeeController = Depends(
            Provide[Container.employee_controller]
        ),
    ):
        self.controller = controller

    @router.get("/", status_code=status.HTTP_200_OK, response_model=List[EmployeeRead])
    async def get_all(self):
        return self.controller.get_all_employees()

    @router.get(
        "/active", status_code=status.HTTP_200_OK, response_model=List[EmployeeRead]
    )
    async def get_active(self):
        return self.controller.find_active_employees()

    @router.get("/{id}", status_code=status.HTTP_200_OK, response_model=EmployeeRead)
    async def get_one(self, id: int):
        employee = self.controller.get_employee_by_id(id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee

    @router.get(
        "/search/{email}", status_code=status.HTTP_200_OK, response_model=EmployeeRead
    )
    async def search_by_email(self, email: str):
        employee = self.controller.find_employee_by_email(email)
        if not employee:
            raise HTTPException(status_code=404, detail="Email not found")
        return employee

    @router.post("/", status_code=status.HTTP_201_CREATED, response_model=EmployeeRead)
    async def create(self, employee: EmployeeCreate):
        return self.controller.create_employee(employee)

    @router.put("/{id}", status_code=status.HTTP_200_OK, response_model=EmployeeRead)
    async def update(self, id: int, employee: EmployeeUpdate):
        updated_employee = self.controller.update_employee(id, employee)
        if not updated_employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return updated_employee

    @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete(self, id: int):
        success = self.controller.delete_employee_by_id(id)
        if not success:
            raise HTTPException(status_code=404, detail="Employee not found")
        return None
