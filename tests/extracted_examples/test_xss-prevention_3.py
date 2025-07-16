"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/xss-prevention.md
"""

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

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
