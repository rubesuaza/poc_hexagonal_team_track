from unittest.mock import MagicMock
from src.application.services.employee.employee_use_cases import EmployeeService
from src.domain.models.employee import Employee
from src.domain.ports.outbounds.unit_of_work_port import UnitOfWorkPort
from datetime import date

class TestEmployeeService:

    def test_create_employee_success(self):
        # Given: A mock UnitOfWork and an employee to create
        mock_uow = MagicMock(spec=UnitOfWorkPort)
        mock_uow.__enter__.return_value = mock_uow
        mock_repository = MagicMock()
        mock_uow.employee_repository = mock_repository
        
        # Assume the employee is active
        mock_repository.find_by_id_and_is_active.return_value = MagicMock()
        
        service = EmployeeService(mock_uow)
        employee = Employee(
            employee_id=1,
            absence_type_id=1,
            is_reportable=True,
            comments="Test comment",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 1, 2),
            hours=None,
            new_profile_type=None
        )

        # When: Creating the employee
        service.create_employee(employee)

        # Then: The repository should be checked for employee status
        mock_repository.find_by_id_and_is_active.assert_called_once_with(1)
        # and the UOW context was used
        mock_uow.__enter__.assert_called_once()
