class EmployeeException(Exception):
    """Base class for business logic exceptions."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)