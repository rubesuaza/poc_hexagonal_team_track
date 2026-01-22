from src.domain.models.employee import Employee
from src.infrastructure.inbounds.rest.dtos.employee.requests.employee_create_request import EmployeeCreateRequest
from src.infrastructure.inbounds.rest.mappers.employee_mapper import EmployeeMapper
from datetime import date
from decimal import Decimal

class TestEmployeeMapper:

    def test_to_domain_success(self):
        # Given: An EmployeeCreateRequest DTO
        request_dto = EmployeeCreateRequest(
            employee_id=1,
            absence_type_id=10,
            is_reportable=True,
            comments="Vacation",
            start_date="2024-01-01",
            end_date="2024-01-05",
            hours=Decimal("8.00"),
            new_profile_type=2
        )

        # When: Mapping to domain
        domain_model = EmployeeMapper.to_domain(request_dto)

        # Then: The domain model should have the same values
        assert isinstance(domain_model, Employee)
        assert domain_model.employee_id == 1
        assert domain_model.absence_type_id == 10
        assert domain_model.is_reportable is True
        assert domain_model.comments == "Vacation"
        assert domain_model.start_date == date(2024, 1, 1)
        assert domain_model.end_date == date(2024, 1, 5)
        assert domain_model.hours == Decimal("8.00")
        assert domain_model.new_profile_type == 2
