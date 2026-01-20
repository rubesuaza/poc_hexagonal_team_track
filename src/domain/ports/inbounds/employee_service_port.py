from abc import ABC, abstractmethod

from src.domain.models.employee import Employee


class EmployeeServicePort(ABC):
    @abstractmethod
    def create_employee(self,employee: Employee) -> Employee:
        """create employee"""
        pass