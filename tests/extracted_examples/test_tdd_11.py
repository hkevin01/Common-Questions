"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

def test_bank_account_withdrawal(self):
    # Arrange
    account = BankAccount(initial_balance=100)
    withdrawal_amount = 30
    
    # Act
    account.withdraw(withdrawal_amount)
    
    # Assert
    self.assertEqual(account.balance, 70)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
