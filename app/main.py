# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


from fastapi import FastAPI
from container import Container
from api.views.employee_views import router as employee_router


def create_app() -> FastAPI:
    # 1. Initialize the DI Container
    container = Container()

    # 2. Wire the container
    # This MUST match the path to the file where @inject is used
    container.wire(modules=["api.views.employee_views"])

    app = FastAPI(
        title="Employee Management System",
        description="Clean Architecture with FastAPI, Dependency Injector, and SQLAlchemy",
        version="1.0.0",
    )

    # 3. Include the routers
    # The 'employee_router' contains all the Class-Based View endpoints
    app.include_router(employee_router)

    # 4. Attach container to app instance (Optional, helpful for debugging/testing)
    app.extra["container"] = container

    return app


app = create_app()

# To run: uvicorn main:app --reload
