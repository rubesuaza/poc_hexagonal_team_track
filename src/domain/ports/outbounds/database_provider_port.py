from abc import ABC, abstractmethod
from typing import Any


class DatabaseProviderPort(ABC):
    """
    Port that defines the contract for providing database connections.
    The Core depends on this, not on SQLAlchemy.
    """

    @abstractmethod
    def get_session(self) -> Any:
        """
        Returns a database session.
        Note: We use 'Any' or a generic because the Domain should not import
        SQLAlchemy types (like Session).
        """
        pass

    @abstractmethod
    def close(self):
        """Closes the connection pool"""
        pass