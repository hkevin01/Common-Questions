"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/xss-prevention.md
"""

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

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
