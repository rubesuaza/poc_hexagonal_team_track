from src.application.services.employee.employee_validations import EmployeeValidation
from src.domain.models.employee import Employee
from src.domain.ports.inbounds.employee_service_port import EmployeeServicePort
from src.domain.ports.outbounds.employee_repository_port import EmployeeRepositoryPort
from src.domain.ports.outbounds.unit_of_work_port import UnitOfWorkPort


class EmployeeService(EmployeeServicePort):

    def __init__(self, uow:UnitOfWorkPort):
        self.uow = uow

    def create_employee(self,employee:Employee) -> Employee:
        with self.uow as uow_context:
            EmployeeValidation.validate_employee_is_active(uow_context.employee_repository, employee.employee_id)
            return employee

