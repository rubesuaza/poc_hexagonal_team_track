from src.domain.models.employee import Employee
from src.infrastructure.outbounds.repositories.employee.entities.employee_entity import EmployeeEntity


class EmployeeMapper:

    @staticmethod
    def to_domain(entity: EmployeeEntity) -> Employee:
        return Employee(
            employee_id=entity.id,
            absence_type_id=0,
            is_reportable=True,
            comments='',
            start_date=entity.date_of_joining,
            end_date=entity.date_of_leaving,
            hours=0.0,
            new_profile_type=None
        )
