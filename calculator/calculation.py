from decimal import Decimal
from typing import Callable
class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a, b, operation)
    @staticmethod
    def perform(self):
        return self.operation(self.a,self.b)