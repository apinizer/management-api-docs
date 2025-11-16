#!/usr/bin/env python3
"""
Convert absolute links to relative links for Jekyll baseurl compatibility.
Jekyll's jekyll-relative-links plugin handles relative links automatically,
but absolute links with baseurl need to be relative.

Changes: /management-api-docs/02-api-reference/... -> 02-api-reference/...
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
BASEURL = "/management-api-docs"

# Pattern to match markdown links
LINK_PATTERN = r'\[([^\]]+)\]\(([^\)]+)\)'


def get_relative_path(from_file: Path, to_path: str) -> str:
    """Calculate relative path from one file to another."""
    # Handle anchors
    anchor = ""
    if '#' in to_path:
        to_path, anchor = to_path.split('#', 1)
        anchor = f"#{anchor}"
    
    # Remove baseurl if present
    if to_path.startswith(BASEURL):
        to_path = to_path[len(BASEURL):]
    
    # Remove leading slash
    to_path = to_path.lstrip('/')
    
    # Get directory of source file
    from_dir = from_file.parent.relative_to(PROJECT_ROOT)
    
    # Calculate relative path
    from_parts = [p for p in str(from_dir).split('/') if p]
    to_parts = [p for p in to_path.split('/') if p]
    
    # Find common prefix
    common_len = 0
    for i in range(min(len(from_parts), len(to_parts))):
        if from_parts[i] == to_parts[i]:
            common_len += 1
        else:
            break
    
    # Build relative path
    up_levels = len(from_parts) - common_len
    rel_parts = ['..'] * up_levels + to_parts[common_len:]
    
    if rel_parts:
        rel_path = '/'.join(rel_parts)
    else:
        rel_path = '.'
    
    return rel_path + anchor


def should_convert_to_relative(link_path: str, current_file: Path) -> bool:
    """Check if link should be converted to relative."""
    # Handle anchors
    if '#' in link_path:
        link_path = link_path.split('#')[0]
    
    # Skip external links
    if '://' in link_path or link_path.startswith('mailto:'):
        return False
    
    # Only convert if it starts with baseurl
    if link_path.startswith(BASEURL):
        return True
    
    return False


def fix_links_in_file(file_path: Path) -> int:
    """Fix all links in a markdown file to use relative paths."""
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
        
        # Check if we should convert to relative
        if should_convert_to_relative(link_path, file_path):
            new_path = get_relative_path(file_path, link_path)
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
    print(f"Converting absolute links to relative links for Jekyll baseurl compatibility...\n")
    
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

