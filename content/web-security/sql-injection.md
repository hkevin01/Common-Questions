# SQL Injection Prevention Guide

## What is SQL Injection?

SQL Injection is a security vulnerability where malicious SQL code is injected into application queries, allowing attackers to manipulate database operations. This can lead to unauthorized data access, data modification, or complete database compromise.

## How SQL Injection Works

### Basic Example
```sql
-- Vulnerable query construction
$query = "SELECT * FROM users WHERE username = '" . $_POST['username'] . "' AND password = '" . $_POST['password'] . "'";

-- If attacker inputs: admin'; --
-- The query becomes:
SELECT * FROM users WHERE username = 'admin'; --' AND password = ''
-- This logs in as admin without knowing the password
```

### Advanced Attack Examples
```sql
-- Data extraction
username: ' UNION SELECT username, password FROM admin_users; --

-- Database structure discovery
username: ' UNION SELECT table_name, column_name FROM information_schema.columns; --

-- File system access (MySQL)
username: ' UNION SELECT LOAD_FILE('/etc/passwd'); --

-- Command execution (if permissions allow)
username: '; EXEC xp_cmdshell('dir'); --
```

## Dangers of SQL Injection

### 1. **Data Breach**
- Access to sensitive customer information
- Credit card numbers, social security numbers, personal data
- Confidential business information

### 2. **Data Manipulation**
- Modifying user accounts and permissions
- Changing prices in e-commerce systems
- Altering financial records

### 3. **Data Destruction**
- Dropping entire tables or databases
- Corrupting critical business data
- Ransomware-style attacks

### 4. **Authentication Bypass**
- Logging in as administrator without credentials
- Accessing restricted areas of applications
- Privilege escalation

### 5. **System Compromise**
- Remote code execution on database server
- Access to server file system
- Lateral movement within network

## Prevention Techniques

### 1. Parameterized Queries (Prepared Statements)

**PHP with MySQLi**:
```php
// Vulnerable code
$username = $_POST['username'];
$password = $_POST['password'];
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($connection, $query);

// Secure code with prepared statements
$username = $_POST['username'];
$password = $_POST['password'];

$stmt = $mysqli->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
$stmt->bind_param("ss", $username, $password);
$stmt->execute();
$result = $stmt->get_result();
```

**PHP with PDO**:
```php
// Secure parameterized query
$username = $_POST['username'];
$password = $_POST['password'];

$stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username AND password = :password");
$stmt->bindParam(':username', $username);
$stmt->bindParam(':password', $password);
$stmt->execute();
$result = $stmt->fetchAll();
```

**Python with SQLite**:
```python
import sqlite3

# Vulnerable code
username = request.form['username']
password = request.form['password']
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

# Secure code with parameterized queries
username = request.form['username']
password = request.form['password']
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
```

**Java with JDBC**:
```java
// Vulnerable code
String username = request.getParameter("username");
String password = request.getParameter("password");
String query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);

// Secure code with PreparedStatement
String username = request.getParameter("username");
String password = request.getParameter("password");
String query = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement pstmt = connection.prepareStatement(query);
pstmt.setString(1, username);
pstmt.setString(2, password);
ResultSet rs = pstmt.executeQuery();
```

### 2. Input Validation and Sanitization

**PHP Input Validation**:
```php
function validateInput($input, $type) {
    switch ($type) {
        case 'email':
            return filter_var($input, FILTER_VALIDATE_EMAIL);
        case 'int':
            return filter_var($input, FILTER_VALIDATE_INT);
        case 'username':
            // Allow only alphanumeric and underscore
            return preg_match('/^[a-zA-Z0-9_]+$/', $input);
        default:
            return false;
    }
}

// Usage
$username = $_POST['username'];
if (!validateInput($username, 'username')) {
    die("Invalid username format");
}

// Additional escaping for legacy code (not recommended as primary defense)
$username = $mysqli->real_escape_string($username);
```

**Python Input Validation**:
```python
import re
from html import escape

def validate_input(input_data, input_type):
    """Validate and sanitize input based on type"""
    if input_type == 'email':
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, input_data) is not None
    elif input_type == 'username':
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return re.match(pattern, input_data) is not None
    elif input_type == 'integer':
        try:
            int(input_data)
            return True
        except ValueError:
            return False
    return False

def sanitize_string(input_string):
    """Sanitize string input by removing dangerous characters"""
    # Remove or escape potentially dangerous characters
    dangerous_chars = ['\'', '"', ';', '\\', '<', '>', '&']
    for char in dangerous_chars:
        input_string = input_string.replace(char, '')
    return input_string.strip()
```

### 3. Stored Procedures

**SQL Server Stored Procedure**:
```sql
-- Create secure stored procedure
CREATE PROCEDURE GetUserByCredentials
    @Username NVARCHAR(50),
    @Password NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT UserID, Username, Email
    FROM Users
    WHERE Username = @Username AND PasswordHash = @Password
END
```

**Calling from Application**:
```php
// PHP calling stored procedure
$stmt = $pdo->prepare("CALL GetUserByCredentials(?, ?)");
$stmt->execute([$username, $hashedPassword]);
$result = $stmt->fetch();
```

### 4. Principle of Least Privilege

**Database User Permissions**:
```sql
-- Create limited database user for application
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'strong_password';

-- Grant only necessary permissions
GRANT SELECT, INSERT, UPDATE ON myapp.users TO 'app_user'@'localhost';
GRANT SELECT ON myapp.products TO 'app_user'@'localhost';

-- DO NOT grant:
-- - DROP, CREATE, ALTER permissions
-- - Access to system tables
-- - FILE privileges
-- - PROCESS privileges
```

### 5. WAF (Web Application Firewall)

**Basic WAF Rules for SQL Injection**:
```apache
# Apache mod_security rules
SecRule ARGS "@detectSQLi" \
    "id:1001,\
    phase:2,\
    block,\
    msg:'SQL Injection Attack Detected',\
    logdata:'Matched Data: %{MATCHED_VAR} found within %{MATCHED_VAR_NAME}'"

# Block common SQL injection patterns
SecRule ARGS "@rx (?i)(union|select|insert|delete|update|drop|create|alter)" \
    "id:1002,\
    phase:2,\
    block,\
    msg:'SQL Keywords Detected'"
```

## Input Validation Best Practices

### 1. Whitelist vs Blacklist

**Whitelist Approach (Recommended)**:
```php
function validateUsername($username) {
    // Only allow letters, numbers, and underscores
    return preg_match('/^[a-zA-Z0-9_]+$/', $username);
}

function validateProductID($id) {
    // Only allow positive integers
    return is_numeric($id) && $id > 0;
}
```

**Blacklist Approach (Not Recommended)**:
```php
function sanitizeInput($input) {
    // Trying to remove all dangerous characters - easy to bypass
    $dangerous = array("'", '"', ';', '--', '/*', '*/', 'xp_', 'sp_');
    return str_replace($dangerous, '', $input);
}
```

### 2. Data Type Validation

```python
def validate_data_types(data):
    """Validate data types before database operations"""
    
    validations = {
        'user_id': lambda x: isinstance(x, int) and x > 0,
        'email': lambda x: isinstance(x, str) and '@' in x and len(x) < 255,
        'age': lambda x: isinstance(x, int) and 0 <= x <= 150,
        'username': lambda x: isinstance(x, str) and x.isalnum() and 3 <= len(x) <= 20
    }
    
    for field, value in data.items():
        if field in validations:
            if not validations[field](value):
                raise ValueError(f"Invalid {field}: {value}")
    
    return True
```

## Testing for SQL Injection

### 1. Manual Testing Payloads

**Basic Test Inputs**:
```
' OR '1'='1
' OR '1'='1' --
' OR '1'='1' /*
'; DROP TABLE users; --
' UNION SELECT null, username, password FROM users --
admin'--
admin'; EXEC xp_cmdshell('dir'); --
```

**Advanced Payloads**:
```
' AND (SELECT COUNT(*) FROM information_schema.tables) > 0 --
' AND (SELECT SUBSTRING(@@version,1,1)) = '5' --
' OR 1=1 LIMIT 1 OFFSET 1 --
' UNION SELECT 1,2,3,4,5,6,7,8,9,10 --
```

### 2. Automated Testing Tools

**SQLMap Usage**:
```bash
# Basic scan
sqlmap -u "http://example.com/login.php" --data="username=admin&password=pass" --dbs

# Dump specific database
sqlmap -u "http://example.com/login.php" --data="username=admin&password=pass" -D myapp --tables

# Extract specific table data
sqlmap -u "http://example.com/login.php" --data="username=admin&password=pass" -D myapp -T users --dump
```

**Custom Testing Script**:
```python
import requests

def test_sql_injection(url, params):
    """Basic SQL injection testing"""
    
    payloads = [
        "' OR '1'='1",
        "' OR '1'='1' --",
        "'; DROP TABLE test; --",
        "' UNION SELECT null, username FROM users --"
    ]
    
    for payload in payloads:
        test_params = params.copy()
        for param in test_params:
            test_params[param] = payload
            
        try:
            response = requests.post(url, data=test_params)
            
            # Check for SQL error messages
            sql_errors = [
                "SQL syntax",
                "mysql_fetch",
                "ORA-",
                "Microsoft OLE DB",
                "PostgreSQL"
            ]
            
            for error in sql_errors:
                if error in response.text:
                    print(f"Potential SQL injection found with payload: {payload}")
                    print(f"Error: {error}")
                    
        except Exception as e:
            print(f"Error testing payload {payload}: {e}")
```

## Legacy Code Protection

### 1. Escaping Functions

**PHP mysqli_real_escape_string()**:
```php
// Emergency fix for legacy code (not ideal, but better than nothing)
function legacySafeQuery($mysqli, $username, $password) {
    // Escape special characters
    $username = $mysqli->real_escape_string($username);
    $password = $mysqli->real_escape_string($password);
    
    // Still vulnerable to some attacks, but reduces risk
    $query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    return $mysqli->query($query);
}

// Better: Gradually migrate to prepared statements
function improvedSafeQuery($mysqli, $username, $password) {
    $stmt = $mysqli->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
    $stmt->bind_param("ss", $username, $password);
    $stmt->execute();
    return $stmt->get_result();
}
```

### 2. XSS Prevention in Output

**PHP htmlspecialchars() and strip_tags()**:
```php
// Prevent XSS when displaying user data
function displaySafeContent($content, $method = 'escape') {
    switch ($method) {
        case 'escape':
            // Convert special chars like < to &lt;
            return htmlspecialchars($content, ENT_QUOTES, 'UTF-8');
            
        case 'strip':
            // Remove all HTML tags
            return strip_tags($content);
            
        case 'whitelist':
            // Allow only specific safe tags
            $allowed_tags = '<p><b><i><u><strong><em>';
            return strip_tags($content, $allowed_tags);
            
        default:
            return htmlspecialchars($content, ENT_QUOTES, 'UTF-8');
    }
}

// Usage examples
$user_comment = $_POST['comment'];

// Display safely escaped content
echo "<p>" . displaySafeContent($user_comment, 'escape') . "</p>";

// Or strip all HTML
echo "<p>" . displaySafeContent($user_comment, 'strip') . "</p>";
```

## Framework-Specific Protection

### Laravel (PHP)
```php
// Laravel Eloquent ORM automatically uses prepared statements
$user = User::where('username', $username)
            ->where('password', Hash::check($password, $user->password))
            ->first();

// Raw queries with parameter binding
$users = DB::select('SELECT * FROM users WHERE username = ? AND active = ?', 
                   [$username, 1]);
```

### Django (Python)
```python
from django.db import models

# Django ORM automatically prevents SQL injection
users = User.objects.filter(username=username, password=password)

# Raw queries with parameter substitution
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", 
               [username, password])
```

### Spring Boot (Java)
```java
@Repository
public class UserRepository {
    
    @Autowired
    private JdbcTemplate jdbcTemplate;
    
    // Safe parameterized query
    public User findByCredentials(String username, String password) {
        String sql = "SELECT * FROM users WHERE username = ? AND password = ?";
        return jdbcTemplate.queryForObject(sql, 
                new Object[]{username, password}, 
                new UserRowMapper());
    }
}
```

## Security Checklist

### ✅ Prevention Checklist
- [ ] All database queries use parameterized statements
- [ ] Input validation is performed on all user inputs
- [ ] Database users have minimal required permissions
- [ ] Error messages don't reveal database structure
- [ ] Regular security testing is performed
- [ ] Code reviews include security considerations
- [ ] WAF rules are configured for SQL injection detection
- [ ] Logging and monitoring for suspicious activity

### ⚠️ Red Flags to Avoid
- [ ] String concatenation for SQL queries
- [ ] Dynamic query building without parameterization
- [ ] Excessive database permissions for application users
- [ ] Detailed error messages in production
- [ ] No input validation or sanitization
- [ ] Trusting client-side validation only
- [ ] Using blacklist-based filtering
- [ ] Ignoring security in code reviews

## Resources and Tools

### Security Testing Tools
- **SQLMap**: Automated SQL injection testing
- **OWASP ZAP**: Web application security scanner
- **Burp Suite**: Professional web security testing
- **Nmap**: Network security scanner with SQL injection scripts

### Learning Resources
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [PortSwigger SQL Injection Guide](https://portswigger.net/web-security/sql-injection)
- [SANS SQL Injection Prevention](https://www.sans.org/white-papers/2966/)

### Secure Coding Guidelines
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [CWE-89: SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- [NIST Secure Software Development](https://csrc.nist.gov/Projects/ssdf)
