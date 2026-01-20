from datetime import date, datetime
from typing import Any

from src.infrastructure.exceptions.infrastructure_exceptions import ValidationException


def validate_max_length_60(v: str | None) -> str | None:
    if v is None:
        return v
    if len(v) > 60:
        raise ValidationException('Comments can only be a maximum of 60 characters')
    return v

def parse_date_flexible(v: Any) -> date | None:
    """Converts strings to date or allows existing dates"""
    if v is None or v == "":
        return None
    if isinstance(v, date):
        return v
    try:
        return datetime.strptime(v, '%Y-%m-%d').date()
    except ValueError:
        raise ValidationException('Invalid date format, should be YYYY-MM-DD')

def validate_positive_id(v: Any) -> int:
    if v is None or not isinstance(v, int) or v <= 0:
        raise ValidationException('Selecting a valid ID is mandatory')
    return v