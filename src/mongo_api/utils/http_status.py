"""http_status.py"""
from fastapi import status


class HttpStatus:
    """HttpStatus for method returning
    """
    def __init__(self, status_code: int, msg: str):
        self.status_code = status_code
        self.msg = msg

    def status_dict(self):
        """Get the response of the endpoint
        """
        return {"status_code": self.status_code, "message": self.msg}


StatusNotFound = HttpStatus(status_code=status.HTTP_404_NOT_FOUND, msg="Not found")
StatusOk = HttpStatus(status_code=status.HTTP_200_OK, msg="Success")
StatusNotOk = HttpStatus(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, msg="Bad request")
StatusCreated = HttpStatus(status_code=status.HTTP_201_CREATED, msg="Created successfully")
StatusUnavailable = HttpStatus(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, msg="Unavailable")
