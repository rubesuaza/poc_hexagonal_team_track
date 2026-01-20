from datetime import date
from typing import Annotated, Optional
from pydantic import BeforeValidator, AfterValidator

from src.infrastructure.inbounds.rest.utils.validators import parse_date_flexible, validate_max_length_60, validate_positive_id

FlexibleDate: type[date]  = Annotated[Optional[date], BeforeValidator(parse_date_flexible)]

ShortComment: type[str]  = Annotated[Optional[str], AfterValidator(validate_max_length_60)]

MandatoryID: type[int] = Annotated[int, BeforeValidator(validate_positive_id)]