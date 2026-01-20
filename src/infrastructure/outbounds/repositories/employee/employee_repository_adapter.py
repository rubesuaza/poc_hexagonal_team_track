import logging

from sqlalchemy.orm import Session

from src.domain.models.employee import Employee
from src.domain.ports.outbounds.employee_repository_port import EmployeeRepositoryPort
from src.infrastructure.outbounds.mappers.employee_mapper import EmployeeMapper
from src.infrastructure.outbounds.repositories.employee.entities.employee_entity import EmployeeEntity

logger = logging.getLogger(__name__)

class EmployeeRepositoryAdapter(EmployeeRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def find_by_id_and_is_active(self, employee_id: int) -> Employee | None:
        db_entity = self.session.query(EmployeeEntity).filter_by(id=employee_id, is_active=True).first()
        if db_entity:
            return EmployeeMapper.to_domain(db_entity)
        else:
            return None
