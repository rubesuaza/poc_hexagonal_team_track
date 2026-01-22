import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from src.infrastructure.inbounds.rest.controllers.employee.employee_recorder_controller import router, app
from src.infrastructure.config.injection_dependency_conf import get_employee_service_port
from src.domain.ports.inbounds.employee_service_port import EmployeeServicePort

# We need to include the router in the app if it's not already there 
# or use the app from main.py. In employee_recorder_controller.py, 'app' and 'router' are defined.
# Let's check if the router is already included in that 'app'.
# Looking at the code, it defines 'app = FastAPI()' and 'router = APIRouter()'.
# It doesn't seem to call app.include_router(router).

client = TestClient(app)

class TestEmployeeRecorderController:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        app.include_router(router)
        self.mock_service = MagicMock(spec=EmployeeServicePort)
        app.dependency_overrides[get_employee_service_port] = lambda: self.mock_service
        yield
        app.dependency_overrides = {}

    def test_record_employee_timeoff_success(self):
        # Given: A valid request payload
        payload = {
            "employee_id": 1,
            "absence_type_id": 2,
            "is_reportable": True,
            "comments": "Test timeoff",
            "start_date": "2024-01-01",
            "end_date": "2024-01-02",
            "hours": 8.0,
            "new_profile_type": 1
        }

        # When: Sending a POST request to the endpoint
        response = client.post("/employee_timeoff/", json=payload)

        # Then: The status code should be 201 and service should be called
        assert response.status_code == 201
        assert response.json()["body"] == "record employee timeoff successfully"
        self.mock_service.create_employee.assert_called_once()
