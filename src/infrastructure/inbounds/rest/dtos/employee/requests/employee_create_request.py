
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from src.infrastructure.inbounds.rest.utils.types import MandatoryID, ShortComment, FlexibleDate


class EmployeeCreateRequest(BaseModel):
    employee_id: int
    absence_type_id: MandatoryID
    is_reportable: Optional[bool] = True
    comments: ShortComment = None
    start_date: FlexibleDate
    end_date: FlexibleDate = None
    hours: Optional[Decimal] = Field(default=Decimal("9.00"), ge=1, le=9)
    new_profile_type: Optional[int] = None

