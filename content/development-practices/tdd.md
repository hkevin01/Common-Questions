# Test Driven Development (TDD) Guide

## What is Test Driven Development?

Test Driven Development (TDD) is a software development methodology where you write tests for your code before writing the actual implementation. The process follows a simple cycle: write a failing test, write minimal code to pass the test, then refactor.

## The TDD Cycle: Red-Green-Refactor

### 🔴 Red: Write a Failing Test
Write a test that describes the behavior you want to implement. The test should fail initially because the functionality doesn't exist yet.

### 🟢 Green: Write Minimal Code to Pass
Write just enough code to make the test pass. Don't worry about perfect design or optimization at this stage.

### 🔵 Refactor: Improve the Code
Clean up the code while keeping all tests passing. Improve design, remove duplication, and enhance readability.

## Benefits of TDD

### 1. **Forces Engineers to Create Unit Tests**
TDD makes testing a natural part of the development process, ensuring comprehensive test coverage.

### 2. **Better Code Design**
Writing tests first forces you to think about the interface and design before implementation, leading to more modular and testable code.

### 3. **Faster Debugging**
When tests fail, you immediately know what broke and where, making debugging much faster.

### 4. **Confidence in Changes**
A comprehensive test suite allows you to refactor and make changes with confidence that you haven't broken existing functionality.

### 5. **Documentation Through Tests**
Tests serve as living documentation, showing how the code is intended to be used.

### 6. **Reduced Bugs**
Catching bugs early in the development process is much cheaper than fixing them in production.

## TDD in Practice: Example Walkthrough

Let's implement a simple calculator using TDD principles.

### Step 1: Red - Write the First Failing Test

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```

**Result**: Test fails because `Calculator` class doesn't exist.

### Step 2: Green - Write Minimal Code

```python
class Calculator:
    def add(self, a, b):
        return a + b

import unittest

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```

**Result**: Test passes! ✅

### Step 3: Red - Add More Tests

```python
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_two_numbers(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        result = self.calc.add(-1, -2)
        self.assertEqual(result, -3)
    
    def test_subtract_two_numbers(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)
```

**Result**: `test_subtract_two_numbers` fails because method doesn't exist.

### Step 4: Green - Implement Subtract

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
```

**Result**: All tests pass! ✅

### Step 5: Refactor - Improve Design

```python
class Calculator:
    """A simple calculator for basic arithmetic operations."""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers and return the result."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and return the result."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```

## Advanced TDD Concepts

### Test Doubles (Mocks, Stubs, Fakes)

```python
import unittest
from unittest.mock import Mock, patch
import requests

class WeatherService:
    def get_temperature(self, city):
        response = requests.get(f"http://api.weather.com/{city}")
        return response.json()['temperature']

class TestWeatherService(unittest.TestCase):
    @patch('requests.get')
    def test_get_temperature(self, mock_get):
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {'temperature': 25}
        mock_get.return_value = mock_response
        
        service = WeatherService()
        
        # Act
        temperature = service.get_temperature('London')
        
        # Assert
        self.assertEqual(temperature, 25)
        mock_get.assert_called_once_with("http://api.weather.com/London")
```

### Parameterized Tests

```python
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_multiple_cases(self):
        test_cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (1.5, 2.5, 4.0),
            (-5, -3, -8)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                result = self.calc.add(a, b)
                self.assertEqual(result, expected)
```

### Testing Exceptions

```python
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_divide_by_zero_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_by_zero_specific_message(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            self.calc.divide(5, 0)
```

## TDD Best Practices

### 1. Write the Simplest Test First
Start with the most basic functionality and gradually add complexity.

```python
# Start simple
def test_empty_list_has_zero_length(self):
    my_list = MyList()
    self.assertEqual(len(my_list), 0)

# Then add complexity
def test_add_item_increases_length(self):
    my_list = MyList()
    my_list.add("item")
    self.assertEqual(len(my_list), 1)
```

### 2. One Test, One Assertion
Keep tests focused on a single behavior.

```python
# Good: Single responsibility
def test_user_creation_sets_name(self):
    user = User("John")
    self.assertEqual(user.name, "John")

def test_user_creation_sets_default_age(self):
    user = User("John")
    self.assertEqual(user.age, 0)

# Avoid: Multiple assertions testing different things
def test_user_creation(self):
    user = User("John")
    self.assertEqual(user.name, "John")  # Testing name
    self.assertEqual(user.age, 0)        # Testing age
    self.assertTrue(user.is_active)      # Testing status
```

### 3. Use Descriptive Test Names

```python
# Good: Describes behavior clearly
def test_withdraw_amount_greater_than_balance_raises_insufficient_funds_error(self):
    pass

def test_successful_withdrawal_reduces_balance_by_amount(self):
    pass

# Poor: Vague names
def test_withdraw(self):
    pass

def test_withdraw_error(self):
    pass
```

### 4. Arrange-Act-Assert Pattern

```python
def test_bank_account_withdrawal(self):
    # Arrange
    account = BankAccount(initial_balance=100)
    withdrawal_amount = 30
    
    # Act
    account.withdraw(withdrawal_amount)
    
    # Assert
    self.assertEqual(account.balance, 70)
```

### 5. Test Edge Cases and Boundaries

```python
class TestStringValidator(unittest.TestCase):
    def test_empty_string_is_invalid(self):
        self.assertFalse(is_valid_name(""))
    
    def test_single_character_is_valid(self):
        self.assertTrue(is_valid_name("A"))
    
    def test_max_length_string_is_valid(self):
        max_name = "A" * 50  # Assuming max length is 50
        self.assertTrue(is_valid_name(max_name))
    
    def test_over_max_length_string_is_invalid(self):
        too_long_name = "A" * 51
        self.assertFalse(is_valid_name(too_long_name))
```

## TDD in Different Languages

### JavaScript with Jest

```javascript
// calculator.test.js
const Calculator = require('./calculator');

describe('Calculator', () => {
    let calc;
    
    beforeEach(() => {
        calc = new Calculator();
    });
    
    test('should add two numbers correctly', () => {
        // Arrange
        const a = 2;
        const b = 3;
        
        // Act
        const result = calc.add(a, b);
        
        // Assert
        expect(result).toBe(5);
    });
    
    test('should throw error when dividing by zero', () => {
        expect(() => {
            calc.divide(10, 0);
        }).toThrow('Cannot divide by zero');
    });
});

// calculator.js
class Calculator {
    add(a, b) {
        return a + b;
    }
    
    divide(a, b) {
        if (b === 0) {
            throw new Error('Cannot divide by zero');
        }
        return a / b;
    }
}

module.exports = Calculator;
```

### Java with JUnit

```java
// CalculatorTest.java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorTest {
    private Calculator calculator;
    
    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }
    
    @Test
    void shouldAddTwoNumbers() {
        // Arrange
        int a = 2;
        int b = 3;
        
        // Act
        int result = calculator.add(a, b);
        
        // Assert
        assertEquals(5, result);
    }
    
    @Test
    void shouldThrowExceptionWhenDividingByZero() {
        // Arrange & Act & Assert
        assertThrows(IllegalArgumentException.class, () -> {
            calculator.divide(10, 0);
        });
    }
}

// Calculator.java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public double divide(double a, double b) {
        if (b == 0) {
            throw new IllegalArgumentException("Cannot divide by zero");
        }
        return a / b;
    }
}
```

## Common TDD Antipatterns

### 1. Writing Tests After Implementation
This defeats the purpose of TDD and often leads to tests that just verify the current implementation rather than the desired behavior.

### 2. Testing Implementation Details
Focus on behavior, not internal implementation.

```python
# Bad: Testing internal implementation
def test_sort_uses_quicksort_algorithm(self):
    sorter = Sorter()
    # This test breaks if we change the algorithm
    self.assertEqual(sorter.algorithm_used, "quicksort")

# Good: Testing behavior
def test_sort_returns_ascending_order(self):
    sorter = Sorter()
    result = sorter.sort([3, 1, 4, 1, 5])
    self.assertEqual(result, [1, 1, 3, 4, 5])
```

### 3. Overly Complex Tests
Tests should be simple and easy to understand.

```python
# Bad: Complex test setup
def test_complex_scenario(self):
    # 20 lines of setup code
    # Multiple objects and interactions
    # Hard to understand what's being tested

# Good: Simple, focused test
def test_user_can_login_with_valid_credentials(self):
    user = User("john@example.com", "password123")
    result = user.login("john@example.com", "password123")
    self.assertTrue(result)
```

## TDD Tools and Frameworks

### Python
- **unittest**: Built-in testing framework
- **pytest**: More flexible and feature-rich
- **nose2**: Extension of unittest
- **mock**: For creating test doubles

### JavaScript
- **Jest**: Popular testing framework with built-in mocking
- **Mocha**: Flexible testing framework
- **Jasmine**: Behavior-driven development framework
- **Cypress**: End-to-end testing

### Java
- **JUnit**: Most popular Java testing framework
- **TestNG**: More advanced testing framework
- **Mockito**: Mocking framework
- **AssertJ**: Fluent assertion library

### .NET
- **NUnit**: Popular .NET testing framework
- **xUnit.net**: Modern testing framework
- **MSTest**: Microsoft's testing framework
- **Moq**: Mocking framework

## Measuring TDD Success

### Code Coverage
```bash
# Python with coverage.py
pip install coverage
coverage run -m pytest
coverage report
coverage html  # Generate HTML report
```

### Test Quality Metrics
- **Test Coverage**: Percentage of code covered by tests
- **Mutation Testing**: Testing the tests themselves
- **Test Execution Time**: Keeping tests fast
- **Test Maintainability**: How easy tests are to update

## Getting Started with TDD

### 1. Start Small
Begin with simple functions and gradually work up to more complex systems.

### 2. Practice with Katas
Use coding exercises specifically designed for TDD practice:
- String Calculator Kata
- Bowling Game Kata
- Roman Numerals Kata
- FizzBuzz Kata

### 3. Set Up Your Environment
Ensure you have:
- Fast test execution
- Immediate feedback
- Easy test running commands
- Good IDE/editor support

### 4. Team Adoption
- Start with new features
- Pair programming sessions
- Code review focus on tests
- Regular TDD practice sessions

## Resources for Learning TDD

### Books
- "Test Driven Development: By Example" by Kent Beck
- "Growing Object-Oriented Software, Guided by Tests" by Freeman & Pryce
- "The Art of Unit Testing" by Roy Osherove

### Online Resources
- [TDD Kata Exercises](http://codingdojo.org/kata/)
- [Uncle Bob's TDD Blog Posts](https://blog.cleancoder.com/)
- [Martin Fowler on TDD](https://martinfowler.com/bliki/TestDrivenDevelopment.html)

### Practice Platforms
- [Cyber-Dojo](https://cyber-dojo.org/)
- [Codewars](https://www.codewars.com/)
- [LeetCode](https://leetcode.com/)

## Conclusion

TDD is more than just a testing technique—it's a design methodology that leads to better, more maintainable code. While it requires discipline and practice to master, the benefits of faster debugging, better design, and increased confidence make it a valuable skill for any developer.

Remember: **Red, Green, Refactor**—and keep your tests simple, fast, and focused on behavior rather than implementation.
