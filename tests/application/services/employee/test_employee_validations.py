import pytest
from unittest.mock import MagicMock
from src.application.services.employee.employee_validations import EmployeeValidation
from src.domain.exceptions.domain_exceptions import EmployeeException
from src.domain.ports.outbounds.employee_repository_port import EmployeeRepositoryPort

class TestEmployeeValidation:

    def test_validate_employee_is_active_success(self):
        # Given: An active employee ID and a repository that finds it
        repository = MagicMock(spec=EmployeeRepositoryPort)
        employee_id = 1
        repository.find_by_id_and_is_active.return_value = MagicMock()

        # When: Validating if the employee is active
        # Then: No exception should be raised
        EmployeeValidation.validate_employee_is_active(repository, employee_id)
        repository.find_by_id_and_is_active.assert_called_once_with(employee_id)

    def test_validate_employee_is_active_not_found(self):
        # Given: An employee ID and a repository that does not find it
        repository = MagicMock(spec=EmployeeRepositoryPort)
        employee_id = 1
        repository.find_by_id_and_is_active.return_value = None

        # When: Validating if the employee is active
        # Then: An EmployeeException should be raised
        with pytest.raises(EmployeeException) as excinfo:
            EmployeeValidation.validate_employee_is_active(repository, employee_id)
        
        assert f"the employee with ID {employee_id} is not active or not exists" in str(excinfo.value)
        repository.find_by_id_and_is_active.assert_called_once_with(employee_id)
