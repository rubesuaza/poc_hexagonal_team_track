from fastapi import FastAPI

from src.domain.exceptions.domain_exceptions import EmployeeException
from src.domain.exceptions.infrastructure_exceptions import  ValidationException, \
    EmployeeOperationException
from src.infrastructure.inbounds.rest.controllers.employee import employee_recorder_controller
from src.infrastructure.inbounds.rest.utils.exception_handlers import employee_exception_handler, \
     validation_exception_handler, employee_operation_exception_handler

app = FastAPI(
    title="Employee Service API",
    description="API to manage employees with Hexagonal Architecture.",
    version="1.0.0"
)


app.add_exception_handler(EmployeeException, employee_exception_handler)
app.add_exception_handler(EmployeeOperationException, employee_operation_exception_handler)
app.add_exception_handler(ValidationException, validation_exception_handler)

app.include_router(
    employee_recorder_controller.router,
    prefix="/api",
    tags=["Employees"]
)

# 3. (Optional) Add your root endpoint
@app.get("/")
async def root():
  return {"message": "Employee API V1. Visit /docs for documentation."}

