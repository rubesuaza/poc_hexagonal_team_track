from abc import ABC, abstractmethod
from typing import Self
from src.domain.ports.outbounds.employee_repository_port import EmployeeRepositoryPort

class UnitOfWorkPort(ABC):
    employee_repository: EmployeeRepositoryPort

    @abstractmethod
    def __enter__(self) -> Self:
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass