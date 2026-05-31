from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Import your concrete implementations
from src.infrastructure.repositories.employee_repository import EmployeeRepository
from src.application.services.employee_service import EmployeeService
from src.application.controllers.employee_controller import EmployeeController

# Database Configuration
DATABASE_URL = "sqlite:///./employee.db"  # Update with your actual connection string
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.api.views.employee_views",
        ]
    )

    # 1. DATABASE SESSION PROVIDER
    # This provides a new session instance for each request
    db_session = providers.Resource(
        lambda: next((s for s in [SessionLocal()] if True), None)
    )

    # 2. REPOSITORY PROVIDER
    # Pass the session explicitly to the repository
    employee_repository = providers.Factory(EmployeeRepository, session=db_session)

    # 3. SERVICE PROVIDER
    employee_service = providers.Factory(
        EmployeeService, repository=employee_repository
    )

    # 4. CONTROLLER PROVIDER
    employee_controller = providers.Factory(
        EmployeeController, service=employee_service
    )
