#!/usr/bin/env python3
"""
Extract and validate code examples from markdown files.
This script extracts code blocks from markdown files and performs
basic syntax validation.
"""

import os
import re
import sys
import tempfile
import subprocess


def extract_code_blocks(file_path, language):
    """Extract code blocks of a specific language from a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match code blocks with language specification
    pattern = rf'```{language}\n(.*?)\n```'
    matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
    
    # Also try without language specification but look for
    # language-specific patterns
    if language == 'python':
        # Look for Python-specific patterns
        general_pattern = r'```\n(.*?)\n```'
        general_matches = re.findall(general_pattern, content, re.DOTALL)
        for match in general_matches:
            keywords = ['def ', 'import ', 'class ', 'print(', 'if __name__']
            if any(keyword in match for keyword in keywords):
                matches.append(match)
    
    return matches


def validate_python_code(code):
    """Validate Python code syntax."""
    try:
        compile(code, '<string>', 'exec')
        return True, "Valid Python syntax"
    except SyntaxError as e:
        return False, f"Python syntax error: {e}"
    except Exception as e:
        return False, f"Python error: {e}"


def validate_javascript_code(code):
    """Validate JavaScript code syntax using Node.js."""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.js',
                                         delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        result = subprocess.run(['node', '--check', temp_file],
                                capture_output=True, text=True)
        os.unlink(temp_file)
        
        if result.returncode == 0:
            return True, "Valid JavaScript syntax"
        else:
            return False, f"JavaScript syntax error: {result.stderr}"
    except Exception as e:
        return False, f"JavaScript validation error: {e}"


def validate_java_code(code):
    """Validate Java code syntax."""
    try:
        # Basic Java syntax checks
        if 'class ' in code:
            # Extract class name
            class_match = re.search(r'class\s+(\w+)', code)
            if class_match:
                class_name = class_match.group(1)
                
                with tempfile.NamedTemporaryFile(mode='w', suffix='.java',
                                                 delete=False) as f:
                    f.write(code)
                    temp_file = f.name
                
                # Rename file to match class name
                temp_dir = os.path.dirname(temp_file)
                java_file = os.path.join(temp_dir, f"{class_name}.java")
                os.rename(temp_file, java_file)
                
                result = subprocess.run(['javac', java_file],
                                        capture_output=True, text=True)
                os.unlink(java_file)
                
                # Clean up compiled class file if it exists
                class_file = os.path.join(temp_dir, f"{class_name}.class")
                if os.path.exists(class_file):
                    os.unlink(class_file)
                
                if result.returncode == 0:
                    return True, "Valid Java syntax"
                else:
                    return False, f"Java compilation error: {result.stderr}"
        
        return True, "Java code snippet (no full class to validate)"
    except Exception as e:
        return False, f"Java validation error: {e}"


def validate_code(code, language):
    """Validate code based on language."""
    validators = {
        'python': validate_python_code,
        'javascript': validate_javascript_code,
        'java': validate_java_code
    }
    
    if language in validators:
        return validators[language](code)
    else:
        return True, f"No validator available for {language}"


def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_and_validate_code.py <language>")
        sys.exit(1)
    
    language = sys.argv[1].lower()
    
    # Find all markdown files
    md_files = []
    for root, dirs, files in os.walk('.'):
        # Skip .git and node_modules directories
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules']]
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    total_blocks = 0
    valid_blocks = 0
    invalid_blocks = 0
    
    print(f"🔍 Validating {language.title()} code blocks...")
    print("=" * 50)
    
    for md_file in md_files:
        code_blocks = extract_code_blocks(md_file, language)
        
        if code_blocks:
            print(f"\n📄 {md_file}")
            
            for i, code in enumerate(code_blocks, 1):
                total_blocks += 1
                
                # Skip very short code blocks (likely just examples)
                if len(code.strip()) < 10:
                    print(f"  ⏭️  Block {i}: Skipping short example")
                    continue
                
                is_valid, message = validate_code(code, language)
                
                if is_valid:
                    valid_blocks += 1
                    print(f"  ✅ Block {i}: {message}")
                else:
                    invalid_blocks += 1
                    print(f"  ❌ Block {i}: {message}")
                    
                    # Show problematic code for debugging
                    print(f"     Code preview: {code[:100]}...")
    
    print("\n" + "=" * 50)
    print(f"📊 Summary for {language.title()}:")
    print(f"   Total blocks found: {total_blocks}")
    print(f"   Valid blocks: {valid_blocks}")
    print(f"   Invalid blocks: {invalid_blocks}")
    
    if invalid_blocks > 0:
        print(f"\n⚠️  Found {invalid_blocks} invalid {language} code blocks!")
        sys.exit(1)
    else:
        print(f"\n🎉 All {language} code blocks are valid!")


if __name__ == "__main__":
    main()
