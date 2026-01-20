from fastapi import Request, status
from fastapi.responses import JSONResponse
from src.domain.exceptions.domain_exceptions import EmployeeException
from src.domain.exceptions.infrastructure_exceptions import DatabaseException, InfrastructureException
from src.infrastructure.inbounds.rest.dtos.response import Response


async def employee_exception_handler(request: Request, exc: EmployeeException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=Response.failure(message=exc.message).model_dump(mode='json')
    )

async def infrastructure_exception_handler(request: Request, exc: InfrastructureException):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )