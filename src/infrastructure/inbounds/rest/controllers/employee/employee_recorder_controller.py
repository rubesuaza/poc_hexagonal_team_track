
from fastapi import FastAPI, APIRouter
from fastapi.params import Depends

from src.domain.ports.inbounds.employee_service_port import EmployeeServicePort
from src.infrastructure.config.injection_dependency_conf import get_employee_service_port

from src.infrastructure.inbounds.rest.dtos.employee.requests.employee_create_request import EmployeeCreateRequest
from src.infrastructure.inbounds.rest.dtos.response import Response
from src.infrastructure.inbounds.rest.mappers.employee_mapper import EmployeeMapper

app = FastAPI()
router = APIRouter()


@router.post(
    "/employee_timeoff/",
    response_model=Response[EmployeeCreateRequest],
    status_code=201,
    summary="Record employee timeoff",
    description="Record employee timeoff",
    )
async def api_record_employee_timeoff(employee_timeoff: EmployeeCreateRequest,
                                      service:EmployeeServicePort = Depends(get_employee_service_port)):
    return Response.success(
        data=EmployeeMapper.to_request(service.create_employee(
            EmployeeMapper.to_domain(employee_timeoff))),
        service_name="Employee Timeoff Recorder")
