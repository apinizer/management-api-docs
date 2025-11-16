#!/usr/bin/env python3
"""
Add .md extension to relative links for Jekyll jekyll-relative-links plugin.
The plugin converts .md links to proper permalinks automatically.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

# Pattern to match markdown links
LINK_PATTERN = r'\[([^\]]+)\]\(([^\)]+)\)'


def should_add_md_extension(link_path: str, current_file: Path) -> bool:
    """Check if link should have .md extension added."""
    # Handle anchors
    if '#' in link_path:
        link_path = link_path.split('#')[0]
    
    # Skip external links
    if '://' in link_path or link_path.startswith('mailto:'):
        return False
    
    # Skip if already has .md
    if link_path.endswith('.md'):
        return False
    
    # Skip if starts with / (absolute)
    if link_path.startswith('/'):
        return False
    
    # Skip if it's a directory path ending with /
    if link_path.endswith('/'):
        return False
    
    # Skip if it's just . or ..
    if link_path in ['.', '..']:
        return False
    
    # Check if target file exists
    current_dir = current_file.parent
    potential_file = current_dir / link_path
    
    # Try with .md extension
    if (potential_file.with_suffix('.md')).exists():
        return True
    
    # Try as directory with index.md
    if (potential_file / 'index.md').exists():
        return False  # Don't add .md, it's a directory
    
    return False


def add_md_extension(link_path: str) -> str:
    """Add .md extension to link path."""
    # Handle anchors
    anchor = ""
    if '#' in link_path:
        link_path, anchor = link_path.split('#', 1)
        anchor = f"#{anchor}"
    
    # Add .md
    if not link_path.endswith('.md'):
        link_path = link_path + '.md'
    
    return link_path + anchor


def fix_links_in_file(file_path: Path) -> int:
    """Fix all links in a markdown file to add .md extension."""
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
        
        # Check if we should add .md extension
        if should_add_md_extension(link_path, file_path):
            new_path = add_md_extension(link_path)
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
    print("Adding .md extension to relative links for Jekyll...\n")
    
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

