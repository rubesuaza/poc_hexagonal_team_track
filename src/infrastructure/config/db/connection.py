import os
import logging
from typing import Any
from dotenv import load_dotenv


from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, scoped_session

from src.domain.exceptions.infrastructure_exceptions import PersistenceException
from src.domain.ports.outbounds.database_provider_port import DatabaseProviderPort


load_dotenv()
logger = logging.getLogger(__name__)


class SqlAlchemyDatabaseProvider(DatabaseProviderPort):
    """
    Concrete adapter that implements DatabaseProviderPort using SQLAlchemy.
    """

    def __init__(self):
        self._engine: Engine | None = None
        self._session_factory = None
        self._initialize_engine()

    @staticmethod
    def _get_db_config() -> dict:
        """Reads configuration from environment variables."""
        config = {
            "user": os.environ.get("DB_USER"),
            "password": os.environ.get("DB_PASSWORD"),
            "host": os.environ.get("DB_HOST"),
            "db_name": os.environ.get("DB_NAME"),
            "port": os.environ.get("DB_PORT", 3306)
        }
        if not all([config['user'], config['password'], config['host'], config['db_name']]):
            logger.error("Missing database environment variables")
            raise PersistenceException("Missing database configuration")
        return config

    def _initialize_engine(self):
        logger.info("Initializing SQLAlchemy engine...")
        try:
            config = self._get_db_config()
            db_url = (
                f"mysql+pymysql://{config['user']}:{config['password']}@"
                f"{config['host']}:{config['port']}/{config['db_name']}"
                f"?charset=utf8mb4"
            )

            self._engine = create_engine(
                db_url,
                pool_recycle=3600,
                pool_pre_ping=True
            )

            session_local = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine
            )

            self._session_factory = scoped_session(session_local)

        except Exception as e:
            logger.error(f"Error creating DB Engine: {e}")
            raise PersistenceException(f"Database connection failed: {str(e)}")

    def get_session(self) -> Any:
        """
        Implementation of the abstract method.
        Returns a new SQLAlchemy session.
        """
        if not self._session_factory:
            self._initialize_engine()
        return self._session_factory()

    def close(self):
        if self._session_factory:
            self._session_factory.remove()
        if self._engine:
            self._engine.dispose()



db_provider = SqlAlchemyDatabaseProvider()