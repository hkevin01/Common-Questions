"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance  # Protected attribute
        self.__account_number = self._generate_account_number()  # Private
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def get_balance(self):
        return self._balance
    
    def _generate_account_number(self):  # Protected method
        return "ACC" + str(random.randint(100000, 999999))

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
