"""Calculator class implementation.

This module provides a Calculator class that uses the operations module.
"""
from __future__ import annotations

from calculator.operations import add, subtract, multiply, divide


class Calculator:
    """A simple calculator class that provides basic arithmetic operations.

    This class uses the functions from the operations module to perform
    calculations and keeps track of calculation history.
    """

    def __init__(self):
        """Initialize a new Calculator with empty history and zeroed memory."""
        self.history: list[str] = []
        # memory register for simple memory store/recall operations
        self.memory: float = 0

    def add(self, a, b):
        result = add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = subtract(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = multiply(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        result = divide(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        """Return the calculation history as a list of strings."""
        return self.history

    # Memory functions expected by the test-suite
    def memory_store(self, value: float) -> None:
        """Store a value in the calculator memory."""
        self.memory = value

    def memory_recall(self) -> float:
        """Recall the value currently stored in memory."""
        return self.memory

    def memory_clear(self) -> None:
        """Clear the calculator memory (set to 0)."""
        self.memory = 0
"""
Calculator class implementation.

This module provides a Calculator class that uses the operations module.
"""
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    """
    A simple calculator class that provides basic arithmetic operations.
    
    This class uses the functions from the operations module to perform
    calculations and keeps track of calculation history.
    """

    def __init__(self):
        """Initialize a new Calculator with empty history."""
        self.history = []
        # memory register for simple memory store/recall operations
        self.memory = 0

    def add(self, a, b):
        """
        Add two numbers and store the operation in history.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        result = add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """
        Subtract b from a and store the operation in history.
        
        Args:
            a: Number to subtract from
            b: Number to subtract
            
        Returns:
            The difference (a - b)
        """
        result = subtract(a, b)
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """
        Multiply two numbers and store the operation in history.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        result = multiply(a, b)
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """
        Divide a by b and store the operation in history.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            The quotient a/b
            
        Raises:
            ZeroDivisionError: If b is 0
        """
        result = divide(a, b)
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        """
        Return the calculation history.
        
        Returns:
            A list of strings representing the calculation history
        """
        return self.history

    # Memory functions expected by the test-suite
    def memory_store(self, value):
        """Store a value in the calculator memory."""
        self.memory = value

    def memory_recall(self):
        """Recall the value currently stored in memory."""
        return self.memory

    def memory_clear(self):
        """Clear the calculator memory (set to 0)."""
        self.memory = 0
# Add to imports in calculator.py
from .scientific import square_root, power

# Add these methods to the Calculator class
def square_root(self, x):
    """Calculate the square root of x."""
    return square_root(x)

def power(self, base, exponent):
    """Calculate base raised to the power of exponent."""
    return power(base, exponent)
def memory_add(self, value):
    """
    Add a value to the memory.
    
    Args:
        value: Value to add to memory
    """
    self.memory += value

def memory_subtract(self, value):
    """
    Subtract a value from the memory.
    
    Args:
        value: Value to subtract from memory
    """
    self.memory -= value
    