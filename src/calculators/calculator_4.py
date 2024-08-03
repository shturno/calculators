from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import Dict, List

class Calculator4:
    
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
    
        median = self.__calculate_median(input_data)
        
        formatted_response = self.__format_response(median)
        
        return formatted_response
        
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Invalid body")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_median(self, numbers: List[float]) -> float:
        median = self.__driver_handler.median(numbers)
        return median
        
    def __format_response(self, median) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": median,
                "Sucess": True
            }  
        }
    