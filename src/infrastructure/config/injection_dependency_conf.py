from fastapi import Depends

from src.application.services.employee.employee_use_cases import EmployeeService
from src.domain.ports.inbounds.employee_service_port import EmployeeServicePort
from src.domain.ports.outbounds.unit_of_work_port import UnitOfWorkPort
from src.infrastructure.outbounds.unity_of_works.sqlalchemy_uow import SqlAlchemyUnitOfWork


def get_unit_of_work() -> UnitOfWorkPort:
    return SqlAlchemyUnitOfWork()

def get_employee_service_port(uow: UnitOfWorkPort = Depends(get_unit_of_work)) -> EmployeeServicePort:
    return EmployeeService(uow=uow)

