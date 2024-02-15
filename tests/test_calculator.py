'''My Calculator Test: Calculator'''
from decimal import Decimal
from pytest import raises
from calculator import Calculator
from calculator.operations import add, subtract
from calculator.calculation import Calculation
from calculator.calculations import Calculations

def test_addition():
    '''Test that add function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that subtract function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that divide function works '''    
    assert Calculator.divide(2,2) == 1
def test_divide_by_zero():
    '''Test that divide by zero throws an exception'''
    with raises(Exception):
        Calculator.divide(2,0)

def test_calculations():
    '''Test that calculation history is able to retrieve the last calculation.'''
    Calculations.clear_history()
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"
def test_get_history():
    '''Test that calculation history is adding calculations properly.'''
    history = Calculations.get_history()
    Calculations.add_calculation(Calculation(Decimal('2'), Decimal('2'), subtract))
    assert len(history) == 2, "History does not contain the expected number of calculations"
