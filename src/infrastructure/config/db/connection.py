import os
import logging
import sys
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager
from collections.abc import Generator



load_dotenv()

logger = logging.getLogger(__name__)


global_engine: Engine | None = None


def get_db_config() -> dict:
    """Reads configuration from environment variables."""
    config = {
        "user": os.environ["DB_USER"],
        "password": os.environ["DB_PASSWORD"],
        "host": os.environ["DB_HOST"],
        "db_name": os.environ["DB_NAME"],
        "port": os.environ.get("DB_PORT", 3306)
    }
    if not all([config['user'], config['password'], config['host'], config['db_name']]):
        logger.error("Missing database environment variables")
        sys.exit(1)
    return config


def get_engine() -> Engine:
    """
    Returns the global SQLAlchemy engine, creating it if it doesn't exist.
    """
    global global_engine
    if global_engine:
        return global_engine

    logger.info("Creating new SQLAlchemy engine...")
    config = get_db_config()


    db_url = (
        f"mysql+pymysql://{config['user']}:{config['password']}@"
        f"{config['host']}:{config['port']}/{config['db_name']}"
        f"?charset=utf8mb4"
    )

    try:
        global_engine = create_engine(
            db_url,
            pool_recycle=3600,  # Recycle connections
            pool_pre_ping=True  # Check connections before using them
        )
        return global_engine
    except Exception as e:
        logger.error(f"Error creating the SQLAlchemy engine: {e}")
        sys.exit(1)



_SessionLocal = None


def get_session_factory():
    """
    Returns the SessionLocal factory, creating it lazily if it doesn't exist.
    """
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=get_engine()
        )
    return _SessionLocal


@contextmanager
def get_db_session() -> Generator[Session, None, None]:
    """
    Session Provider. Provides a session and
    ensures it is closed properly.
    """
    SessionLocal = get_session_factory()
    session = SessionLocal()
    logger.info("Starting new DB session")
    try:
        yield session
    except Exception:
        logger.error("Error in DB session, performing rollback...")
        session.rollback()
        raise
    finally:
        logger.info("Closing DB session")
        session.close()
