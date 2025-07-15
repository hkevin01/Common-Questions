# FizzBuzz Challenge

## Problem Description

Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

## Expected Output
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
```

## Solutions

### Python Solution
```python
def fizzbuzz():
    """
    Classic FizzBuzz implementation
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Alternative using string concatenation
def fizzbuzz_alternative():
    """
    Alternative implementation using string building
    """
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)

if __name__ == "__main__":
    fizzbuzz()
```

### JavaScript Solution
```javascript
function fizzBuzz() {
    for (let i = 1; i <= 100; i++) {
        if (i % 15 === 0) {
            console.log("FizzBuzz");
        } else if (i % 3 === 0) {
            console.log("Fizz");
        } else if (i % 5 === 0) {
            console.log("Buzz");
        } else {
            console.log(i);
        }
    }
}

// Alternative using array and join
function fizzBuzzAlternative() {
    for (let i = 1; i <= 100; i++) {
        let output = [];
        if (i % 3 === 0) output.push("Fizz");
        if (i % 5 === 0) output.push("Buzz");
        console.log(output.length ? output.join("") : i);
    }
}

fizzBuzz();
```

### Java Solution
```java
public class FizzBuzz {
    public static void main(String[] args) {
        fizzBuzz();
    }
    
    public static void fizzBuzz() {
        for (int i = 1; i <= 100; i++) {
            if (i % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }
}
```

## Variations and Extensions

### FizzBuzz with Different Numbers
Modify the classic problem to use different divisors:
```python
def custom_fizzbuzz(n, rules):
    """
    Generalized FizzBuzz with custom rules
    
    Args:
        n: Upper limit for counting
        rules: List of tuples (divisor, word)
    """
    for i in range(1, n + 1):
        output = ""
        for divisor, word in rules:
            if i % divisor == 0:
                output += word
        print(output or i)

# Example: FizzBuzzBang (3->Fizz, 5->Buzz, 7->Bang)
custom_fizzbuzz(50, [(3, "Fizz"), (5, "Buzz"), (7, "Bang")])
```

### FizzBuzz as a Test Problem
```python
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_output(self):
        """Test FizzBuzz generates correct output"""
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", 
                   "11", "Fizz", "13", "14", "FizzBuzz"]
        
        result = []
        for i in range(1, 16):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
                
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
```

## Key Learning Points

1. **Modulo Operation**: Understanding remainder division (`%` operator)
2. **Conditional Logic**: Multiple if-else conditions and precedence
3. **Loop Structures**: Iteration from 1 to n
4. **String Manipulation**: Building output strings
5. **Edge Cases**: Handling multiples of both numbers (15 = 3×5)

## Common Mistakes

1. **Wrong Order**: Checking `% 3` and `% 5` before `% 15` can miss "FizzBuzz"
2. **Off-by-One**: Starting from 0 instead of 1, or using `< 100` instead of `<= 100`
3. **Type Issues**: Mixing strings and integers in output

## Interview Tips

- Start with the basic solution, then optimize
- Consider edge cases and boundary conditions  
- Discuss alternative approaches (string building vs conditional)
- Talk about extensibility (what if we add more rules?)
- Mention testing and validation approaches

## Resources

- [Original FizzBuzz on Rosetta Code](https://www.rosettacode.org/wiki/FizzBuzz)
- [FizzBuzz: One Simple Interview Question](https://blog.codinghorror.com/why-cant-programmers-program/)
