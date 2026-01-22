from typing import Callable, Any

from sqlalchemy.exc import IntegrityError, OperationalError

from src.domain.exceptions.operation_exceptions import  PersistenceException
from src.domain.ports.outbounds.database_provider_port import DatabaseProviderPort
from src.domain.ports.outbounds.unit_of_work_port import UnitOfWorkPort



class SqlAlchemyUnitOfWork(UnitOfWorkPort):
    def __init__(self,
                 db_provider:DatabaseProviderPort,
                 repository_factory:Callable[[Any],Any]):
        self.db_provider = db_provider
        self.repository_factory = repository_factory
        self.session=None

    def __enter__(self):

        self.session = self.db_provider.get_session()

        self.employee_repository = self.repository_factory(self.session)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.rollback()
            else:
                self.commit()
        finally:
            self.session.close()

    def commit(self):
        try:
            self.session.commit()
        except IntegrityError | OperationalError as e:
            raise PersistenceException('error committing the transaction to the database') from e

    def rollback(self):
        try:
            self.session.rollback()
        except IntegrityError | OperationalError as e:
            raise PersistenceException('error doing rollback the transaction to the database') from e