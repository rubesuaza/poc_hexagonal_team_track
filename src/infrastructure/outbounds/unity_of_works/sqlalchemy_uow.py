from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import Session

from src.infrastructure.exceptions.infrastructure_exceptions import DatabaseException
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
        try:
            self.session.commit()
        except IntegrityError | OperationalError as e:
            raise DatabaseException('error committing the transaction to the database') from e

    def rollback(self):
        try:
            self.session.rollback()
        except IntegrityError | OperationalError as e:
            raise DatabaseException('error doing rollback the transaction to the database') from e