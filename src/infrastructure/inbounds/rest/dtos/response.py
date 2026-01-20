import uuid
from datetime import datetime
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel, Field


T = TypeVar("T")


class Header(BaseModel):
    transaction_uuid: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    service: str

class Response(BaseModel, Generic[T]):
    header: Header = Field(default_factory=Header)
    body: T
    error_message: Optional[str] = None


    @classmethod
    def success(cls, data: T, service_name: str = "Service"):
        return cls(
            header=Header(service=service_name),
            body=data
        )

    @classmethod
    def failure(cls, message: str, service_name: str = "Service"):
        return cls(
            header=Header(service=service_name),
            body=None,
            error_message=message
        )