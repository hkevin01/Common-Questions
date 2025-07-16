#!/usr/bin/env python3
"""
Script to validate code examples in markdown files.
Extracts code blocks and performs syntax validation.
"""

import os
import re
import ast
import sys
import tempfile
import subprocess
from pathlib import Path
from typing import List, Dict


class CodeValidator:
    """Validates code examples in markdown files."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        
    def extract_code_blocks(self, content: str) -> List[Dict]:
        """Extract code blocks from markdown content."""
        pattern = r'```(\w+)?\n(.*?)```'
        blocks = []
        
        for match in re.finditer(pattern, content, re.DOTALL):
            language = match.group(1) or 'text'
            code = match.group(2).strip()
            
            blocks.append({
                'language': language.lower(),
                'code': code,
                'line_number': content[:match.start()].count('\n') + 1
            })
            
        return blocks
    def validate_python_code(self, code: str, filename: str,
                             line_number: int) -> bool:
        """Validate Python code syntax."""
        try:
            ast.parse(code)
            return True
        except SyntaxError as e:
            self.errors.append(
                f"{filename}:{line_number + e.lineno - 1}: "
                f"Python syntax error: {e.msg}"
            )
            return False
        except Exception as e:
            self.warnings.append(
                f"{filename}:{line_number}: "
                f"Python validation warning: {str(e)}"
            )
            return True

    def validate_javascript_code(self, code: str, filename: str,
                                line_number: int) -> bool:
        """Validate JavaScript code syntax using Node.js."""
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.js',
                                           delete=False) as f:
                f.write(code)
                temp_file = f.name

            result = subprocess.run(
                ['node', '--check', temp_file],
                capture_output=True,
                text=True
            )

            os.unlink(temp_file)

            if result.returncode != 0:
                self.errors.append(
                    f"{filename}:{line_number}: "
                    f"JavaScript syntax error: {result.stderr.strip()}"
                )
                return False

            return True

        except FileNotFoundError:
            self.warnings.append(
                f"{filename}:{line_number}: "
                "Node.js not found, skipping JavaScript validation"
            )
            return True
        except Exception as e:
            self.warnings.append(
                f"{filename}:{line_number}: "
                f"JavaScript validation error: {str(e)}"
            )
            return True

    def validate_java_code(self, code: str, filename: str,
                          line_number: int) -> bool:
        """Basic Java syntax validation."""
        # Check for common syntax issues
        if 'public class' in code and not code.strip().endswith('}'):
            self.warnings.append(
                f"{filename}:{line_number}: "
                "Java class might be missing closing brace"
            )

        # Check for common method patterns
        if 'public static void main' in code:
            if ('(String[] args)' not in code and
                    '(String args[])' not in code):
                self.errors.append(
                    f"{filename}:{line_number}: "
                    "Java main method signature incorrect"
                )
                return False

        return True

    def validate_sql_code(self, code: str, filename: str,
                         line_number: int) -> bool:
        """Basic SQL syntax validation."""
        # Check for common SQL patterns
        sql_keywords = [
            'SELECT', 'INSERT', 'UPDATE', 'DELETE',
            'CREATE', 'DROP', 'ALTER'
        ]
        upper_code = code.upper()

        has_sql_keyword = any(
            keyword in upper_code for keyword in sql_keywords
        )

        if has_sql_keyword:
            # Check for common issues
            if ('SELECT' in upper_code and 'FROM' not in upper_code and
                    '*' in code):
                self.warnings.append(
                    f"{filename}:{line_number}: "
                    "SELECT * without FROM clause might be incomplete"
                )

        return True
    
    def validate_markdown_file(self, filepath: Path) -> bool:
        """Validate all code blocks in a markdown file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.errors.append(f"Error reading {filepath}: {str(e)}")
            return False
        
        blocks = self.extract_code_blocks(content)
        all_valid = True
        
        for block in blocks:
            language = block['language']
            code = block['code']
            line_number = block['line_number']
            
            if language == 'python':
                if not self.validate_python_code(code, str(filepath), line_number):
                    all_valid = False
            elif language in ['javascript', 'js']:
                if not self.validate_javascript_code(code, str(filepath), line_number):
                    all_valid = False
            elif language == 'java':
                if not self.validate_java_code(code, str(filepath), line_number):
                    all_valid = False
            elif language in ['sql', 'mysql', 'postgresql']:
                if not self.validate_sql_code(code, str(filepath), line_number):
                    all_valid = False
        
        return all_valid
    
    def validate_directory(self, directory: Path) -> bool:
        """Validate all markdown files in a directory."""
        all_valid = True
        
        for md_file in directory.rglob('*.md'):
            # Skip node_modules and other ignored directories
            if any(part.startswith('.') or part == 'node_modules' for part in md_file.parts):
                continue
                
            if not self.validate_markdown_file(md_file):
                all_valid = False
        
        return all_valid
    
    def print_results(self):
        """Print validation results."""
        if self.errors:
            print("❌ Validation Errors:")
            for error in self.errors:
                print(f"  {error}")
            print()
        
        if self.warnings:
            print("⚠️  Validation Warnings:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        if not self.errors and not self.warnings:
            print("✅ All code examples are valid!")
        elif not self.errors:
            print(f"✅ No errors found. {len(self.warnings)} warnings.")
        else:
            print(f"❌ {len(self.errors)} errors, {len(self.warnings)} warnings found.")


def main():
    """Main function."""
    validator = CodeValidator()
    
    # Get current directory
    current_dir = Path.cwd()
    
    print(f"Validating code examples in: {current_dir}")
    print("=" * 50)
    
    # Validate all markdown files
    is_valid = validator.validate_directory(current_dir)
    
    # Print results
    validator.print_results()
    
    # Exit with appropriate code
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
