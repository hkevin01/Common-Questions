"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/personal-development.md
"""

def calculate_loan_payment(principal, rate, term):
    """
    Calculate monthly loan payment using standard amortization formula.
    
    Args:
        principal (float): Loan amount in dollars
        rate (float): Annual interest rate (as decimal, e.g., 0.05 for 5%)
        term (int): Loan term in years
    
    Returns:
        float: Monthly payment amount
        
    Note: Formula assumes monthly compounding. For other compounding
    frequencies, use calculate_loan_payment_custom() instead.
    """
    # Convert annual rate to monthly and years to months
    monthly_rate = rate / 12
    num_payments = term * 12
    
    # Handle edge case: zero interest rate
    if rate == 0:
        return principal / num_payments
    
    # Standard amortization formula
    # Bug fix 2024-07-10: Previous version didn't handle rate conversion correctly
    payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
              ((1 + monthly_rate)**num_payments - 1)
    
    return round(payment, 2)  # Round to cents for currency

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
