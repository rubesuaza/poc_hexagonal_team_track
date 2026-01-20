from sqlalchemy.orm import Session
from src.domain.ports.outbounds.unit_of_work_port import UnitOfWorkPort
from src.infrastructure.config.db.connection import get_session_factory  # Tu factory actual
from src.infrastructure.outbounds.repositories.employee.employee_repository_adapter import EmployeeRepositoryAdapter


class SqlAlchemyUnitOfWork(UnitOfWorkPort):
    def __init__(self, session_factory=None):
        self.session_factory = session_factory or get_session_factory()

    def __enter__(self):

        self.session: Session = self.session_factory()

        self.employee_repository = EmployeeRepositoryAdapter(self.session)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.rollback()
            else:
                self.commit()  # Opcional: Auto-commit al salir exitoso
        finally:
            self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()