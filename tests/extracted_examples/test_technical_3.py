"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
