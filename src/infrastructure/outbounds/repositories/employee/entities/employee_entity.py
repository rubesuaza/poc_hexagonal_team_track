from datetime import datetime


from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, TIMESTAMP, func, DateTime
from sqlalchemy.orm import DeclarativeBase, declarative_base

Base = declarative_base()

class EmployeeEntity(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    document = Column(String(255), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    # user_id = Column(ForeignKey('users.id'), index=True)
    # employee_profile_id = Column(ForeignKey('employee_profiles.id'), index=True)
    date_of_joining = Column(Date, nullable=True)
    date_of_leaving = Column(DateTime, nullable=True, default=datetime(2999, 1, 1))
    is_active = Column(Boolean, default=True)
    is_assignable = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())