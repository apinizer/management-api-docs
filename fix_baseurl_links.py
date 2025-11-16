#!/usr/bin/env python3
"""
Fix all absolute links to include baseurl prefix.
Jekyll baseurl is "/management-api-docs", so all absolute links should start with it.
Changes: /01-getting-started/ -> /management-api-docs/01-getting-started/
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
BASEURL = "/management-api-docs"

# Pattern to match markdown links
LINK_PATTERN = r'\[([^\]]+)\]\(([^\)]+)\)'

# Pattern to match absolute paths that should have baseurl
ABSOLUTE_PATH_PATTERN = r'^/(0[1-3]-[^/]+|index\.md)'


def should_add_baseurl(link_path: str) -> bool:
    """Check if link path should have baseurl added."""
    # Handle anchors
    if '#' in link_path:
        link_path = link_path.split('#')[0]
    
    # Skip external links
    if '://' in link_path or link_path.startswith('mailto:'):
        return False
    
    # Only add baseurl to absolute paths starting with /01-, /02-, /03-, or /index
    if link_path.startswith('/'):
        # Check if it's an internal documentation path
        if re.match(ABSOLUTE_PATH_PATTERN, link_path) or link_path.startswith('/01-') or link_path.startswith('/02-') or link_path.startswith('/03-'):
            # Don't add if already has baseurl
            if not link_path.startswith(BASEURL):
                return True
    
    return False


def add_baseurl_to_path(link_path: str) -> str:
    """Add baseurl prefix to link path."""
    # Handle anchors
    anchor = ""
    if '#' in link_path:
        link_path, anchor = link_path.split('#', 1)
        anchor = f"#{anchor}"
    
    # Add baseurl
    if link_path.startswith('/'):
        new_path = BASEURL + link_path
    else:
        new_path = link_path
    
    return new_path + anchor


def fix_links_in_file(file_path: Path) -> int:
    """Fix all links in a markdown file to include baseurl."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return 0
    
    original_content = content
    fixed_count = 0
    
    def replace_link(match):
        nonlocal fixed_count
        link_text = match.group(1)
        link_path = match.group(2)
        
        # Check if we should add baseurl
        if should_add_baseurl(link_path):
            new_path = add_baseurl_to_path(link_path)
            fixed_count += 1
            return f'[{link_text}]({new_path})'
        
        return match.group(0)
    
    # Replace all markdown links
    content = re.sub(LINK_PATTERN, replace_link, content)
    
    # Write if changed
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return fixed_count
        except Exception as e:
            print(f"❌ Error writing {file_path}: {e}")
            return 0
    
    return 0


def main():
    """Main function."""
    print(f"Adding baseurl '{BASEURL}' to all absolute links...\n")
    
    total_files = 0
    total_fixed = 0
    
    # Process all markdown files
    for md_file in sorted(PROJECT_ROOT.rglob('*.md')):
        # Skip hidden and special files
        if any(part.startswith('.') for part in md_file.parts):
            continue
        if md_file.name in ['SESSION_SUMMARY.md']:
            continue
        
        total_files += 1
        links_fixed = fix_links_in_file(md_file)
        total_fixed += links_fixed
        
        if links_fixed > 0:
            print(f"✓ Fixed {links_fixed} links in {md_file.relative_to(PROJECT_ROOT)}")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files processed: {total_files}")
    print(f"  Total links fixed: {total_fixed}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

