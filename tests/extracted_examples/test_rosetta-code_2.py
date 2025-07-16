"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/rosetta-code.md
"""

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(limit):
    """Generate all primes up to limit using Sieve of Eratosthenes"""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, limit + 1) if sieve[i]]

# Find primes up to 100
primes = sieve_of_eratosthenes(100)
print(f"Primes up to 100: {primes}")

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
