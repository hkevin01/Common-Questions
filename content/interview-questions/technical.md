# Technical Interview Questions Guide

A comprehensive collection of technical interview questions covering programming fundamentals, system design, and domain-specific topics.

## HTTP Status Codes

### Common HTTP Status Codes
Understanding HTTP status codes is essential for web development and API design.

**200 - OK (Success)**
- Request succeeded
- Most common successful response
- Used for successful GET, POST, PUT requests

**403 - Forbidden (Not Authorized)**
- Server understood request but refuses to authorize it
- Authentication won't help (unlike 401)
- User doesn't have permission to access resource

**404 - Not Found**
- Server cannot find requested resource
- Most common error status
- URL doesn't exist or resource has been moved

### Extended HTTP Status Code Knowledge

**1xx Informational**
- `100 Continue`: Client should continue with request
- `101 Switching Protocols`: Server switching protocols per client request

**2xx Success**
- `201 Created`: Request succeeded and new resource was created
- `202 Accepted`: Request accepted but not yet processed
- `204 No Content`: Success but no content to return

**3xx Redirection**
- `301 Moved Permanently`: Resource permanently moved to new URL
- `302 Found`: Resource temporarily moved
- `304 Not Modified`: Resource hasn't been modified (caching)

**4xx Client Errors**
- `400 Bad Request`: Malformed request syntax
- `401 Unauthorized`: Authentication required
- `405 Method Not Allowed`: HTTP method not supported
- `429 Too Many Requests`: Rate limiting activated

**5xx Server Errors**
- `500 Internal Server Error`: Generic server error
- `502 Bad Gateway`: Invalid response from upstream server
- `503 Service Unavailable`: Server temporarily unavailable
- `504 Gateway Timeout`: Upstream server timeout

### Interview Questions on HTTP Status Codes

**Q: What's the difference between 401 and 403 status codes?**
```
A: 401 Unauthorized means authentication is required and has failed or not been provided.
   403 Forbidden means the server understood the request but refuses to authorize it.
   With 401, providing credentials might help. With 403, authorization won't help.
```

**Q: When would you use 201 vs 200 for a POST request?**
```
A: 201 Created should be used when a POST request successfully creates a new resource.
   200 OK can be used when POST processes data but doesn't create a specific resource,
   or when the response contains relevant data about the operation.
```

**Q: Explain the difference between 302 and 301 redirects.**
```
A: 301 Moved Permanently tells clients and search engines that the resource has
   permanently moved to a new location. Browsers and crawlers should update bookmarks/links.
   302 Found indicates temporary relocation. Original URL should be used for future requests.
```

## Programming Language Fundamentals

### Object-Oriented Programming Concepts

**Q: Explain the four pillars of OOP.**

**1. Encapsulation**
```python
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
```

**2. Inheritance**
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

**3. Polymorphism**
```python
def animal_sound(animal):
    return animal.speak()  # Same method, different behavior

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal_sound(animal))  # Polymorphic behavior
```

**4. Abstraction**
```python
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
```

### Data Structures and Algorithms

**Q: Implement a stack and explain its use cases.**

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack - O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self.items)

# Use cases:
# - Function call management (call stack)
# - Undo operations in applications
# - Expression evaluation and syntax parsing
# - Browser history (back button)
# - Depth-First Search (DFS) algorithms
```

**Q: What's the difference between Array and Linked List?**

```python
# Array characteristics:
# - Contiguous memory allocation
# - O(1) random access by index
# - O(n) insertion/deletion (except at end)
# - Better cache locality

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):  # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def search(self, data):  # O(n)
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# Linked List characteristics:
# - Non-contiguous memory allocation
# - O(n) access by position
# - O(1) insertion/deletion at known position
# - Dynamic size, no memory waste
```

### Algorithm Complexity Analysis

**Q: Explain Big O notation with examples.**

```python
# O(1) - Constant Time
def get_first_element(arr):
    return arr[0] if arr else None

# O(log n) - Logarithmic Time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear Time
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# O(n log n) - Linearithmic Time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# O(n²) - Quadratic Time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(2^n) - Exponential Time
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```

## Database and SQL Questions

### Basic SQL Queries

**Q: Write SQL to find the second highest salary.**

```sql
-- Method 1: Using LIMIT and OFFSET
SELECT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1;

-- Method 2: Using subquery
SELECT MAX(salary) as second_highest
FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Method 3: Using ROW_NUMBER() window function
SELECT salary
FROM (
    SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
    FROM employees
) ranked
WHERE rn = 2;
```

**Q: Find employees who earn more than their managers.**

```sql
SELECT e.name as employee_name, e.salary as employee_salary,
       m.name as manager_name, m.salary as manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
WHERE e.salary > m.salary;
```

### Database Design Questions

**Q: Explain database normalization.**

**First Normal Form (1NF)**
- Each column contains atomic (indivisible) values
- Each row is unique
- No repeating groups

**Second Normal Form (2NF)**
- Must be in 1NF
- No partial dependencies on composite primary keys
- Non-key attributes fully dependent on primary key

**Third Normal Form (3NF)**
- Must be in 2NF
- No transitive dependencies
- Non-key attributes not dependent on other non-key attributes

```sql
-- Before normalization (violates 1NF - repeating groups)
CREATE TABLE orders_bad (
    order_id INT,
    customer_name VARCHAR(100),
    product1 VARCHAR(100),
    product2 VARCHAR(100),
    product3 VARCHAR(100)
);

-- After normalization
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
```

## System Design Questions

### Scalability Concepts

**Q: How would you design a URL shortening service like bit.ly?**

**Requirements:**
- Shorten long URLs to short URLs
- Redirect short URLs to original URLs
- Handle 100M URLs per day
- High availability and low latency

**High-Level Design:**
```
Client -> Load Balancer -> Web Servers -> Cache -> Database
                                    \-> Analytics Service
```

**Database Schema:**
```sql
CREATE TABLE urls (
    id BIGINT PRIMARY KEY,
    short_url VARCHAR(7) UNIQUE,
    long_url TEXT,
    created_at TIMESTAMP,
    expires_at TIMESTAMP,
    user_id INT
);

CREATE INDEX idx_short_url ON urls(short_url);
CREATE INDEX idx_user_id ON urls(user_id);
```

**Algorithm for Short URL Generation:**
```python
import string
import random

def generate_short_url(length=7):
    """Generate random short URL"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def base62_encode(num):
    """Convert number to base62 string"""
    if num == 0:
        return '0'
    
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while num > 0:
        result = chars[num % 62] + result
        num //= 62
    
    return result
```

### Caching Strategies

**Q: Explain different caching strategies.**

**1. Cache-Aside (Lazy Loading)**
```python
def get_user(user_id):
    # Check cache first
    user = cache.get(f"user:{user_id}")
    if user is None:
        # Cache miss - fetch from database
        user = database.get_user(user_id)
        # Store in cache
        cache.set(f"user:{user_id}", user, ttl=3600)
    return user

def update_user(user_id, data):
    # Update database
    database.update_user(user_id, data)
    # Invalidate cache
    cache.delete(f"user:{user_id}")
```

**2. Write-Through**
```python
def update_user(user_id, data):
    # Update database
    database.update_user(user_id, data)
    # Update cache
    cache.set(f"user:{user_id}", data, ttl=3600)
```

**3. Write-Behind (Write-Back)**
```python
def update_user(user_id, data):
    # Update cache immediately
    cache.set(f"user:{user_id}", data, ttl=3600)
    # Queue database update for later
    queue.add_task("update_user_db", user_id, data)
```

## Coding Problem Solutions

### String Manipulation

**Q: Implement a function to check if a string is a palindrome.**

```python
def is_palindrome(s):
    """Check if string is palindrome (case-insensitive, alphanumeric only)"""
    # Clean string: remove non-alphanumeric, convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Two-pointer approach
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
test_cases = [
    "A man a plan a canal Panama",  # True
    "race a car",                   # False
    "hello",                        # False
    "Madam",                        # True
    ""                              # True (empty string)
]

for test in test_cases:
    print(f"'{test}' -> {is_palindrome(test)}")
```

### Array Problems

**Q: Find two numbers in an array that sum to a target value.**

```python
def two_sum(nums, target):
    """Find indices of two numbers that add up to target"""
    # Hash map approach - O(n) time, O(n) space
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found

# Two-pointer approach for sorted array
def two_sum_sorted(nums, target):
    """Find two numbers in sorted array that sum to target"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

### Tree Problems

**Q: Implement binary tree traversal methods.**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """Left -> Root -> Right"""
    result = []
    
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result

def preorder_traversal(root):
    """Root -> Left -> Right"""
    result = []
    
    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result

def postorder_traversal(root):
    """Left -> Right -> Root"""
    result = []
    
    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    
    postorder(root)
    return result

def level_order_traversal(root):
    """Breadth-first traversal"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result
```

## Behavioral and Experience Questions

### Problem-Solving Framework

**Q: Describe a challenging technical problem you solved.**

**Framework (STAR Method):**
- **Situation**: Set the context and background
- **Task**: Describe what needed to be accomplished
- **Action**: Explain what you did specifically
- **Result**: Share the outcome and what you learned

**Example Response Structure:**
```
Situation: "In my previous role, our application was experiencing..."
Task: "I needed to identify the root cause and implement a solution that..."
Action: "I approached this by first..., then I..., and finally I..."
Result: "This resulted in... and I learned that..."
```

### Technical Leadership Questions

**Q: How do you handle code reviews?**

**Good Practices:**
- Focus on code, not the person
- Provide constructive feedback with suggestions
- Explain the "why" behind suggestions
- Acknowledge good practices
- Be consistent with team standards

**Example Response:**
```
"I approach code reviews as collaborative learning opportunities. I focus on:
1. Code correctness and functionality
2. Readability and maintainability
3. Performance considerations
4. Security implications
5. Adherence to team standards

I always provide specific examples and suggestions for improvement,
and I make sure to acknowledge well-written code and clever solutions."
```

## Advanced Topics

### Concurrency and Threading

**Q: Explain the difference between processes and threads.**

```python
import threading
import multiprocessing
import time

# Threading example
def worker_thread(name):
    for i in range(5):
        print(f"Thread {name}: {i}")
        time.sleep(1)

# Create and start threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker_thread, args=(f"T{i}",))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Multiprocessing example
def worker_process(name):
    for i in range(5):
        print(f"Process {name}: {i}")
        time.sleep(1)

# Create and start processes
processes = []
for i in range(3):
    p = multiprocessing.Process(target=worker_process, args=(f"P{i}",))
    processes.append(p)
    p.start()

# Wait for all processes to complete
for p in processes:
    p.join()
```

**Key Differences:**
- **Memory**: Threads share memory, processes have separate memory spaces
- **Communication**: Threads use shared variables, processes use IPC
- **Overhead**: Threads have lower creation/switching overhead
- **Isolation**: Processes provide better isolation and fault tolerance
- **GIL**: Python's GIL limits true parallelism in threads for CPU-bound tasks

### Security Questions

**Q: How would you implement secure password storage?**

```python
import bcrypt
import secrets
import hashlib

def hash_password(password):
    """Securely hash a password using bcrypt"""
    # Generate salt and hash password
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    return password_hash

def verify_password(password, password_hash):
    """Verify password against stored hash"""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash)

def generate_secure_token():
    """Generate cryptographically secure random token"""
    return secrets.token_urlsafe(32)

# Example usage
password = "user_password_123"
hashed = hash_password(password)
is_valid = verify_password(password, hashed)
```

**Security Best Practices:**
- Use strong hashing algorithms (bcrypt, scrypt, Argon2)
- Always use salts to prevent rainbow table attacks
- Implement rate limiting for login attempts
- Use secure random number generators
- Enforce strong password policies
- Implement proper session management

## Interview Preparation Tips

### Before the Interview
1. **Review Fundamentals**: Data structures, algorithms, system design
2. **Practice Coding**: Use platforms like LeetCode, HackerRank
3. **Prepare Examples**: Have specific examples of past work ready
4. **Research Company**: Understand their technology stack and challenges
5. **Prepare Questions**: Show interest by asking thoughtful questions

### During the Interview
1. **Clarify Requirements**: Ask questions to understand the problem fully
2. **Think Out Loud**: Explain your thought process
3. **Start Simple**: Begin with basic solution, then optimize
4. **Test Your Code**: Walk through examples and edge cases
5. **Discuss Trade-offs**: Explain pros and cons of different approaches

### Common Mistakes to Avoid
- Jumping into coding without understanding the problem
- Not considering edge cases or error handling
- Focusing only on optimal solution without starting simple
- Not communicating thought process clearly
- Getting stuck on one approach instead of trying alternatives

### Questions to Ask Interviewers
- What does a typical day look like in this role?
- What are the biggest technical challenges the team is facing?
- How do you measure success in this position?
- What opportunities are there for learning and growth?
- Can you tell me about the team I'd be working with?

---

## Summary

Technical interviews assess both your knowledge and problem-solving approach. Focus on:

1. **Strong Fundamentals**: Master data structures, algorithms, and core concepts
2. **Problem-Solving Skills**: Practice breaking down complex problems
3. **Communication**: Clearly explain your thinking and approach
4. **Practical Experience**: Be ready to discuss real projects and challenges
5. **Continuous Learning**: Show enthusiasm for learning new technologies

Remember that interviews are conversations, not tests. The goal is to demonstrate your ability to think through problems and work effectively with the team.
