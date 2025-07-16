#!/usr/bin/env python3
"""
Extract code examples from markdown files for testing.
"""

import re
import sys
from pathlib import Path


def extract_python_examples():
    """Extract Python code examples for testing."""
    current_dir = Path.cwd()
    test_dir = current_dir / "tests" / "extracted_examples"
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Create __init__.py
    (test_dir / "__init__.py").touch()
    
    extracted_count = 0
    
    for md_file in current_dir.rglob('*.md'):
        if any(part.startswith('.') for part in md_file.parts):
            continue
            
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except IOError:
            continue
            
        # Extract Python code blocks
        pattern = r'```python\n(.*?)```'
        for i, match in enumerate(re.finditer(pattern, content, re.DOTALL)):
            code = match.group(1).strip()
            
            # Skip empty or import-only blocks
            if not code or len(code.split('\n')) < 3:
                continue
                
            # Create test file
            safe_filename = re.sub(r'[^\w\-_.]', '_', md_file.stem)
            test_filename = f"test_{safe_filename}_{i}.py"
            test_file = test_dir / test_filename
            
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(f'"""\nExtracted from {md_file}\n"""\n\n')
                f.write(code)
                f.write('\n\n# Test function\ndef test_syntax():\n')
                f.write('    """Test that code compiles '
                        'without syntax errors."""\n')
                f.write('    pass\n')
            
            extracted_count += 1
    
    print(f"✅ Extracted {extracted_count} Python code examples")
    return extracted_count > 0


if __name__ == "__main__":
    success = extract_python_examples()
    sys.exit(0 if success else 1)
