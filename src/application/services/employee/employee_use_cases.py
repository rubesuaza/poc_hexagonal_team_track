from src.application.services.employee.employee_validations import EmployeeValidation
from src.domain.exceptions.domain_exceptions import EmployeeException
from src.domain.exceptions.infrastructure_exceptions import InfrastructureException
from src.domain.models.employee import Employee
from src.domain.ports.inbounds.employee_service_port import EmployeeServicePort
from src.domain.ports.outbounds.unit_of_work_port import UnitOfWorkPort


class EmployeeService(EmployeeServicePort):

    def __init__(self, uow:UnitOfWorkPort):
        self.uow = uow

    def create_employee(self,employee:Employee) -> Employee:
        with self.uow as uow_context:
            try:
                EmployeeValidation.validate_employee_is_active(
                    uow_context.employee_repository, employee.employee_id)
            except EmployeeException as e:
                raise EmployeeException(str(e))
            except Exception as e:
                raise InfrastructureException(f'error in infrastructure - Error: {e}')
            return employee

