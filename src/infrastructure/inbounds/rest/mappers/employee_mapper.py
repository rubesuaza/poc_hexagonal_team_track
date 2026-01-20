# src/infrastructure/rest/mappers/employee_mapper.py
from src.domain.models.employee import Employee
from src.infrastructure.inbounds.rest.dtos.employee.requests.employee_create_request import EmployeeCreateRequest


class EmployeeMapper:

    @staticmethod
    def to_domain(request: EmployeeCreateRequest) -> Employee:
        return Employee(
            employee_id=request.employee_id,
            absence_type_id=request.absence_type_id,
            is_reportable=request.is_reportable,
            comments=request.comments,
            start_date=request.start_date,
            end_date=request.end_date,
            hours=request.hours,
            new_profile_type=request.new_profile_type
        )

    @staticmethod
    def to_request(entity: Employee) -> EmployeeCreateRequest:
        return EmployeeCreateRequest(
            employee_id=entity.employee_id,
            absence_type_id=entity.absence_type_id,
            is_reportable=entity.is_reportable,
            comments=entity.comments,
            start_date=entity.start_date,
            end_date=entity.end_date,
            hours=entity.hours,
            new_profile_type=entity.new_profile_type
        )