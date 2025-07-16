#!/usr/bin/env python3
"""
Script to check internal links in markdown files.
"""

import re
import sys
from pathlib import Path


def check_internal_links():
    """Check all internal links in markdown files."""
    current_dir = Path.cwd()
    errors = []

    # Find all markdown files
    md_files = list(current_dir.rglob('*.md'))

    # Extract all internal links
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    for md_file in md_files:
        if any(part.startswith('.') for part in md_file.parts):
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except IOError as e:
            errors.append(f"Error reading {md_file}: {e}")
            continue

        for match in re.finditer(link_pattern, content):
            link_url = match.group(2)

            # Skip external links
            if link_url.startswith(('http://', 'https://', 'mailto:')):
                continue

            # Check if internal file exists
            if link_url.startswith('/'):
                # Absolute link from root
                target_path = current_dir / link_url.lstrip('/')
            else:
                # Relative link
                target_path = md_file.parent / link_url

            # Remove anchor fragments for file checking
            file_path = str(target_path).split('#')[0]
            target_file = Path(file_path)

            if not target_file.exists():
                line_num = content[:match.start()].count('\n') + 1
                errors.append(
                    f"{md_file}:{line_num}: "
                    f"Broken link '{link_url}' -> {target_file}"
                )

    if errors:
        print("❌ Internal Link Errors:")
        for error in errors:
            print(f"  {error}")
        sys.exit(1)
    else:
        print("✅ All internal links are valid!")
        sys.exit(0)


if __name__ == "__main__":
    check_internal_links()
