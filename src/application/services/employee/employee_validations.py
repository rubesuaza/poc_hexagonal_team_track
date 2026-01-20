from src.domain.exceptions.domain_exceptions import EmployeeException
from src.domain.ports.outbounds.employee_repository_port import EmployeeRepositoryPort


class EmployeeValidation:


    @staticmethod
    def validate_employee_is_active(repository: EmployeeRepositoryPort,employee_id: int):
        if repository.find_by_id_and_is_active(employee_id) is None:
            raise EmployeeException(f'the employee with ID {employee_id} is not active or not exists')
