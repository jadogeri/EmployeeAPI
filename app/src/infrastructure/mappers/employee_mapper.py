from domain.entities.employee import Employee
from models.employee_model import EmployeeModel


class EmployeeMapper:
    @staticmethod
    def to_entity(db_model: EmployeeModel) -> Employee:
        return Employee(
            id=db_model.id,
            first_name=db_model.first_name,
            last_name=db_model.last_name,
            email=db_model.email,
            role=db_model.role,
            is_active=db_model.is_active
        )
