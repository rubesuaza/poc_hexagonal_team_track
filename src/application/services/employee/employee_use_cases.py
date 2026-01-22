from src.application.services.employee.employee_validations import EmployeeValidation
from src.domain.exceptions.domain_exceptions import EmployeeException
from src.domain.exceptions.infrastructure_exceptions import EmployeeOperationException
from src.domain.models.employee import Employee
from src.domain.ports.inbounds.employee_service_port import EmployeeServicePort
from src.domain.ports.outbounds.unit_of_work_port import UnitOfWorkPort


class EmployeeService(EmployeeServicePort):

    def __init__(self, uow:UnitOfWorkPort):
        self.uow = uow

    def create_employee(self,employee:Employee) :
        with self.uow as uow_context:
            try:
                EmployeeValidation.validate_employee_is_active(
                    uow_context.employee_repository, employee.employee_id)
            except EmployeeException as e:
                raise e
            except Exception as e:
                raise EmployeeOperationException(f'error creating employee: {e}') from e


