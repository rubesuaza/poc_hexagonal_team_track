from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import Optional



@dataclass
class Employee:
    employee_id: int
    absence_type_id: int
    is_reportable: Optional[bool]
    comments: str
    start_date: date
    end_date: date
    hours: Optional[Decimal]
    new_profile_type: Optional[int]
