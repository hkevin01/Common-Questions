# Rosetta Code - Programming Chrestomathy

## What is Rosetta Code?

[Rosetta Code](https://www.rosettacode.org/wiki/Rosetta_Code) is a programming chrestomathy site. The idea is to present solutions to the same task in many different programming languages, to demonstrate how languages are similar and different, and to aid a person with a grounding in one approach to a problem in learning another.

## Why Use Rosetta Code?

1. **Language Comparison**: See how different languages approach the same problem
2. **Learning New Languages**: Understand syntax and idioms across languages
3. **Algorithm Practice**: Work on well-defined programming challenges
4. **Best Practices**: Learn from community-contributed solutions
5. **Interview Prep**: Practice common programming problems

## Popular Problems from Rosetta Code

### 1. FizzBuzz
**Problem**: Print numbers 1-100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".

**See**: [FizzBuzz Solutions](fizzbuzz.md)

### 2. Hello World
**Problem**: Display "Hello, World!" - the classic first program.

**Python**:
```python
print("Hello, World!")
```

**JavaScript**:
```javascript
console.log("Hello, World!");
```

**Java**:
```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### 3. Fibonacci Sequence
**Problem**: Generate the Fibonacci sequence.

**Python**:
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Iterative approach (more efficient)
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
print(list(fibonacci_iterative(10)))
```

**JavaScript**:
```javascript
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Iterative generator
function* fibonacciGenerator() {
    let [a, b] = [0, 1];
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}

// Get first 10 numbers
const fib = fibonacciGenerator();
const first10 = Array.from({length: 10}, () => fib.next().value);
console.log(first10);
```

### 4. Prime Numbers
**Problem**: Find or test for prime numbers.

**Python**:
```python
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
```

### 5. Sorting Algorithms
**Problem**: Implement various sorting algorithms.

**Bubble Sort**:
```python
def bubble_sort(arr):
    """Bubble sort implementation"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**Quick Sort**:
```python
def quick_sort(arr):
    """Quick sort implementation"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
```

### 6. String Manipulation
**Problem**: Various string processing tasks.

**Palindrome Check**:
```python
def is_palindrome(s):
    """Check if string is a palindrome (ignoring case and non-alphanumeric)"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Test cases
test_strings = ["A man a plan a canal Panama", "race a car", "hello"]
for s in test_strings:
    print(f"'{s}' is palindrome: {is_palindrome(s)}")
```

**Anagram Detection**:
```python
def are_anagrams(str1, str2):
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    # Sort characters and compare
    return sorted(str1) == sorted(str2)

# Alternative using character count
from collections import Counter
def are_anagrams_counter(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    return Counter(str1) == Counter(str2)
```

## How to Approach Rosetta Code Problems

1. **Understand the Problem**: Read the requirements carefully
2. **Plan Your Solution**: Think about the algorithm before coding
3. **Start Simple**: Implement a basic solution first
4. **Optimize**: Improve efficiency and readability
5. **Test**: Verify with different inputs
6. **Compare**: Look at solutions in other languages
7. **Learn**: Understand different approaches and idioms

## Categories of Problems

### Mathematical
- Number theory (primes, factors, GCD)
- Sequences (Fibonacci, Pascal's triangle)
- Calculations (roots, powers, factorials)

### String Processing
- Pattern matching and searching
- Text transformation and formatting
- Encoding and decoding

### Data Structures
- Array and list manipulation
- Tree and graph traversal
- Hash tables and sets

### Algorithms
- Sorting and searching
- Dynamic programming
- Recursive solutions

### Input/Output
- File processing
- Data parsing
- Format conversion

## Benefits for Interview Preparation

1. **Pattern Recognition**: Learn common problem patterns
2. **Multiple Solutions**: Understand different approaches
3. **Language Fluency**: Practice syntax across languages
4. **Optimization**: Learn to improve time/space complexity
5. **Communication**: Practice explaining solutions

## Getting Started

1. Visit [Rosetta Code](https://www.rosettacode.org/wiki/Rosetta_Code)
2. Browse problems by category or difficulty
3. Start with simpler problems (Hello World, FizzBuzz)
4. Implement solutions in your preferred language
5. Compare with existing solutions
6. Try implementing in a new language
7. Focus on understanding different approaches

## Resources

- [Rosetta Code Main Site](https://www.rosettacode.org/wiki/Rosetta_Code)
- [Popular Programming Tasks](https://www.rosettacode.org/wiki/Category:Programming_Tasks)
- [Language Comparison](https://www.rosettacode.org/wiki/Language_Comparison_Table)
- [Draft Tasks](https://www.rosettacode.org/wiki/Category:Draft_Programming_Tasks)
