"""Tests for calculator operations."""
from calculator.operations import add, subtract
import pytest

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    """Test the subtract function."""
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -100, 0)
])
def test_add_parameterized(a, b, expected):
    """Test add function with multiple inputs."""
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 3),
    (0, 0, 0),
    (1, 1, 0),
    (-1, -1, 0)
])
def test_subtract_parameterized(a, b, expected):
    """Test subtract function with multiple inputs."""
    assert subtract(a, b) == expected  
