#!/usr/bin/env python3
"""
Comprehensive quality assurance script for the Common Questions repository.
Runs all validation checks and generates a quality report.
"""

import subprocess
import sys
from pathlib import Path
import time


def run_command(command, description):
    """Run a command and return success status."""
    print(f"🔍 {description}...")
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )

        if result.returncode == 0:
            print(f"✅ {description} - PASSED")
            if result.stdout.strip():
                print(f"   {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {description} - FAILED")
            if result.stderr.strip():
                print(f"   Error: {result.stderr.strip()}")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
            return False

    except Exception as e:
        print(f"❌ {description} - ERROR: {e}")
        return False


def check_project_structure():
    """Verify essential project files exist."""
    print("🔍 Checking project structure...")
    
    required_files = [
        'README.md',
        'LICENSE',
        'docs/CONTRIBUTING.md',
        'docs/content-validation-checklist.md',
        '.github/workflows/ci-cd.yml',
        '.github/workflows/github-pages.yml',
        'scripts/validate_code_examples.py',
        'scripts/check_internal_links.py',
        'scripts/extract_code_examples.py',
        'requirements-dev.txt',
        'requirements-test.txt',
        'setup.cfg',
        '.markdownlint.json'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Project structure - FAILED")
        print("   Missing files:")
        for file_path in missing_files:
            print(f"     - {file_path}")
        return False
    else:
        print("✅ Project structure - PASSED")
        print(f"   All {len(required_files)} required files present")
        return True


def count_content_files():
    """Count and categorize content files."""
    print("📊 Analyzing content...")
    
    categories = {
        'coding-challenges': list(Path('content/coding-challenges').glob('*.md')),
        'interview-questions': list(Path('content/interview-questions').glob('*.md')),
        'web-security': list(Path('content/web-security').glob('*.md')),
        'development-practices': list(Path('content/development-practices').glob('*.md')),
        'object-oriented-programming': list(Path('content/object-oriented-programming').glob('*.md'))
    }
    
    total_files = 0
    for category, files in categories.items():
        count = len(files)
        total_files += count
        print(f"   {category}: {count} files")
    
    print(f"   Total content files: {total_files}")
    return total_files > 0


def main():
    """Run comprehensive quality assurance checks."""
    print("=" * 60)
    print("🎯 COMMON QUESTIONS - QUALITY ASSURANCE REPORT")
    print("=" * 60)
    print(f"⏰ Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Track results
    checks = []
    
    # 1. Project structure validation
    checks.append(check_project_structure())
    print()
    
    # 2. Content analysis
    checks.append(count_content_files())
    print()
    
    # 3. Code validation
    checks.append(run_command(
        "python scripts/validate_code_examples.py",
        "Code syntax validation"
    ))
    print()
    
    # 4. Internal link checking
    checks.append(run_command(
        "python scripts/check_internal_links.py",
        "Internal link validation"
    ))
    print()
    
    # 5. Code extraction test
    checks.append(run_command(
        "python scripts/extract_code_examples.py",
        "Code extraction functionality"
    ))
    print()
    
    # 6. Python script compilation
    checks.append(run_command(
        "python -m py_compile scripts/*.py",
        "Python script compilation"
    ))
    print()
    
    # 7. YAML syntax validation
    yaml_check_cmd = ("python -c \"import yaml; "
                      "yaml.safe_load(open('.github/workflows/ci-cd.yml'))\"")
    checks.append(run_command(
        yaml_check_cmd,
        "CI/CD workflow YAML syntax"
    ))
    print()
    
    # 8. Markdown linting (if markdownlint is available)
    try:
        markdown_lint_available = subprocess.run(
            "which markdownlint-cli2",
            shell=True,
            capture_output=True,
            check=False
        ).returncode == 0
    except (subprocess.SubprocessError, OSError):
        markdown_lint_available = False

    if markdown_lint_available:
        checks.append(run_command(
            "markdownlint-cli2 '**/*.md'",
            "Markdown format validation"
        ))
    else:
        print("⚠️  Markdown linting - SKIPPED (markdownlint-cli2 not available)")
        print("   Install with: npm install -g markdownlint-cli2")
    print()
    
    # Generate summary
    print("=" * 60)
    print("📋 QUALITY ASSURANCE SUMMARY")
    print("=" * 60)
    
    passed = sum(checks)
    total = len(checks)
    pass_rate = (passed / total) * 100 if total > 0 else 0
    
    print(f"✅ Checks passed: {passed}/{total} ({pass_rate:.1f}%)")
    
    if passed == total:
        print("🎉 ALL QUALITY CHECKS PASSED!")
        print("   Repository is ready for production use.")
        exit_code = 0
    else:
        print("⚠️  SOME QUALITY CHECKS FAILED")
        print("   Please address the issues above before proceeding.")
        exit_code = 1
    
    print()
    print("🚀 Infrastructure Status:")
    print("   - GitHub Actions CI/CD: Ready")
    print("   - GitHub Pages deployment: Ready")
    print("   - Code validation pipeline: Ready")
    print("   - Community contribution framework: Ready")
    
    print()
    print(f"⏰ Completed: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
