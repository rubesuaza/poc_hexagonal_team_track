import pytest
from datetime import date
from src.infrastructure.inbounds.rest.utils.validators import (
    validate_max_length_60,
    parse_date_flexible,
    validate_positive_id
)
from src.domain.exceptions.operation_exceptions import ValidationException

class TestValidators:

    def test_validate_max_length_60_success(self):
        # Given: A string within limits
        text = "a" * 60
        # When/Then: No exception
        assert validate_max_length_60(text) == text

    def test_validate_max_length_60_failure(self):
        # Given: A string exceeding limits
        text = "a" * 61
        # When/Then: ValidationException
        with pytest.raises(ValidationException) as excinfo:
            validate_max_length_60(text)
        assert "Comments can only be a maximum of 60 characters" in str(excinfo.value)

    def test_parse_date_flexible_string(self):
        # Given: A date string
        d_str = "2024-05-20"
        # When/Then: Correct date object
        assert parse_date_flexible(d_str) == date(2024, 5, 20)

    def test_parse_date_flexible_invalid(self):
        # Given: An invalid date string
        d_str = "20-05-2024"
        # When/Then: ValidationException
        with pytest.raises(ValidationException) as excinfo:
            parse_date_flexible(d_str)
        assert "Invalid date format, should be YYYY-MM-DD" in str(excinfo.value)

    def test_validate_positive_id_success(self):
        # Given: A positive integer
        v = 10
        # When/Then: Returns the integer
        assert validate_positive_id(v) == 10

    def test_validate_positive_id_failure(self):
        # Given: Zero or negative or non-int
        for v in [0, -1, "abc", None]:
            with pytest.raises(ValidationException):
                validate_positive_id(v)
