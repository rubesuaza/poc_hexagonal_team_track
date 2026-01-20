from abc import ABC, abstractmethod

from src.domain.models.employee import Employee


class EmployeeRepositoryPort(ABC):
    @abstractmethod
    def find_by_id_and_is_active(self, employee_id: int) -> Employee | None:
        pass