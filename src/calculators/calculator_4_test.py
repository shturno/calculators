from .calculator_4 import Calculator4
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import Dict, List

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
        
class MockDriverHandlerError:
    def median(self, numbers: List[float]) -> float:
        return 15
    
class MockDriverHandler:
    def median(self, numbers: List[float]) -> float:
        return 100
    
    
def test_calculate():
    mock_request = MockRequest({ "numbers": [100] })
    calculator_4 = Calculator4(MockDriverHandler())
    
    response = calculator_4.calculate(mock_request)
    
    assert response == { "data": { "Calculator": 4, "value": 100, "Sucess": True } }
        
    