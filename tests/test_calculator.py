"""Tests for the Calculator class and some operations."""
import pytest
from calculator.calculator import Calculator
from calculator.operations import add, subtract, multiply

@pytest.fixture
def calculator():
    """Create and return a Calculator instance for testing."""
    return Calculator()

def test_calculator_initialization(calculator):
    """Test that calculator initializes with memory set to 0."""
    assert calculator.memory_recall() == 0

def test_calculator_operations(calculator):
    """Test the basic calculator operations."""
    assert calculator.add(1, 2) == 3
    assert calculator.subtract(5, 3) == 2
    assert calculator.multiply(2, 4) == 8
    assert calculator.divide(10, 2) == 5

def test_memory_store_and_recall(calculator):
    """Test the memory store and recall functions."""
    calculator.memory_store(5)
    assert calculator.memory_recall() == 5

def test_memory_clear(calculator):
    """Test the memory clear function."""
    calculator.memory_store(5)
    calculator.memory_clear()
    assert calculator.memory_recall() == 0
def test_add_large_numbers():
    """Test addition with large numbers."""
    assert add(10**10, 10**10) == 2 * 10**10

def test_subtract_identical_numbers():
    """Test subtraction of identical numbers always gives zero."""
    assert subtract(100, 100) == 0
    assert subtract(-42, -42) == 0

def test_multiply_by_zero():
    """Test that multiplying by zero always gives zero."""
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(0, 0) == 0
    