from .http_unprocessable_entity import HttpUnprocessableEntityError
from .http_bad_request import HttpBadRequestError
from typing import Dict

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {
                "error": [{
                    "name": error.name,
                    "message": error.message
                }]
            }
        }
    else:
        return {
            "status_code": 500,
            "error": [{
                "name": "Internal Server Error",
                "message": str(error)
            }]
        }