#!/usr/bin/env python3
"""
Fix wrong path segments in links.
Finds and fixes common path mistakes like:
- /02-api-reference/01-getting-started/ -> /01-getting-started/
- /02-api-reference/04-api-proxies/05-policies/ -> /02-api-reference/05-policies/
- /03-appendix/01-getting-started/ -> /01-getting-started/
- /03-appendix/02-api-reference/ -> /02-api-reference/
"""

import re
from pathlib import Path
from typing import Dict

PROJECT_ROOT = Path(__file__).parent

# Pattern to match markdown links
LINK_PATTERN = r'\[([^\]]+)\]\(([^\)]+)\)'

# Common wrong path patterns and their corrections
PATH_FIXES = [
    # Wrong: /02-api-reference/01-getting-started/ -> /01-getting-started/
    (r'/02-api-reference/01-getting-started/', '/01-getting-started/'),
    (r'/02-api-reference/01-getting-started', '/01-getting-started/'),
    
    # Wrong: /03-appendix/01-getting-started/ -> /01-getting-started/
    (r'/03-appendix/01-getting-started/', '/01-getting-started/'),
    (r'/03-appendix/01-getting-started', '/01-getting-started/'),
    
    # Wrong: /02-api-reference/04-api-proxies/05-policies/ -> /02-api-reference/05-policies/
    (r'/02-api-reference/04-api-proxies/05-policies/', '/02-api-reference/05-policies/'),
    (r'/02-api-reference/04-api-proxies/05-policies', '/02-api-reference/05-policies/'),
    
    # Wrong: /02-api-reference/04-api-proxies/06-connections/ -> /02-api-reference/06-connections/
    (r'/02-api-reference/04-api-proxies/06-connections/', '/02-api-reference/06-connections/'),
    (r'/02-api-reference/04-api-proxies/06-connections', '/02-api-reference/06-connections/'),
    
    # Wrong: /02-api-reference/04-api-proxies/07-credentials/ -> /02-api-reference/07-credentials/
    (r'/02-api-reference/04-api-proxies/07-credentials/', '/02-api-reference/07-credentials/'),
    (r'/02-api-reference/04-api-proxies/07-credentials', '/02-api-reference/07-credentials/'),
    
    # Wrong: /02-api-reference/04-api-proxies/08-certificates/ -> /02-api-reference/08-certificates/
    (r'/02-api-reference/04-api-proxies/08-certificates/', '/02-api-reference/08-certificates/'),
    (r'/02-api-reference/04-api-proxies/08-certificates', '/02-api-reference/08-certificates/'),
    
    # Wrong: /03-appendix/02-api-reference/ -> /02-api-reference/
    (r'/03-appendix/02-api-reference/', '/02-api-reference/'),
    (r'/03-appendix/02-api-reference', '/02-api-reference/'),
    
    # Wrong: /02-api-reference/01-getting-started/authentication/ -> /01-getting-started/authentication/
    (r'/02-api-reference/01-getting-started/([^)]+)', r'/01-getting-started/\1'),
    
    # Wrong: /03-appendix/01-getting-started/... -> /01-getting-started/...
    (r'/03-appendix/01-getting-started/([^)]+)', r'/01-getting-started/\1'),
    
    # Wrong: /02-api-reference/04-api-proxies/05-policies/... -> /02-api-reference/05-policies/...
    (r'/02-api-reference/04-api-proxies/05-policies/([^)]+)', r'/02-api-reference/05-policies/\1'),
    (r'/02-api-reference/04-api-proxies/06-connections/([^)]+)', r'/02-api-reference/06-connections/\1'),
    (r'/02-api-reference/04-api-proxies/07-credentials/([^)]+)', r'/02-api-reference/07-credentials/\1'),
    (r'/02-api-reference/04-api-proxies/08-certificates/([^)]+)', r'/02-api-reference/08-certificates/\1'),
    
    # Wrong: /03-appendix/02-api-reference/... -> /02-api-reference/...
    (r'/03-appendix/02-api-reference/([^)]+)', r'/02-api-reference/\1'),
]


def fix_path_in_link(link_path: str) -> str:
    """Fix wrong path segments in a link path."""
    original = link_path
    
    # Handle anchors
    anchor = ""
    if '#' in link_path:
        link_path, anchor = link_path.split('#', 1)
        anchor = f"#{anchor}"
    
    # Apply all fixes
    for wrong_pattern, correct_pattern in PATH_FIXES:
        link_path = re.sub(wrong_pattern, correct_pattern, link_path)
    
    # Ensure ends with / if it's a path (not external)
    if link_path.startswith('/') and not link_path.endswith('/') and '://' not in link_path:
        link_path = link_path + '/'
    
    return link_path + anchor


def fix_links_in_file(file_path: Path) -> int:
    """Fix wrong paths in all links in a file."""
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
        
        # Skip external links
        if '://' in link_path or link_path.startswith('mailto:'):
            return match.group(0)
        
        # Fix the path
        new_path = fix_path_in_link(link_path)
        
        # Count if changed
        if link_path != new_path:
            fixed_count += 1
        
        return f'[{link_text}]({new_path})'
    
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
    print("Fixing wrong path segments in links...\n")
    
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

