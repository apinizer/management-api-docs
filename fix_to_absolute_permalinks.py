#!/usr/bin/env python3
"""
Convert all relative links to absolute permalinks with baseurl.
Jekyll's jekyll-relative-links plugin doesn't always work reliably on GitHub Pages,
so we'll use absolute permalinks with baseurl prefix.

Converts:
- crud/list-api-proxies.md -> /management-api-docs/02-api-reference/04-api-proxies/crud/list-api-proxies/
- ../../01-getting-started/authentication.md -> /management-api-docs/01-getting-started/authentication/
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
BASEURL = "/management-api-docs"

# Pattern to match markdown links
LINK_PATTERN = r'\[([^\]]+)\]\(([^\)]+)\)'


def get_permalink_from_file(file_path: Path) -> str:
    """Get Jekyll permalink from file path or front matter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for permalink in front matter
        permalink_match = re.search(r'permalink:\s*([^\n]+)', content)
        if permalink_match:
            permalink = permalink_match.group(1).strip().strip('"\'')
            if permalink.startswith('/'):
                return BASEURL + permalink.rstrip('/') + '/'
    except Exception:
        pass
    
    # Generate permalink from file path
    rel_path = file_path.relative_to(PROJECT_ROOT)
    path_str = str(rel_path).replace('.md', '')
    
    # Handle index files
    if path_str.endswith('/index') or path_str == 'index':
        path_str = path_str.replace('/index', '').replace('index', '')
    
    # Convert to permalink
    if path_str:
        permalink = BASEURL + '/' + path_str.replace('\\', '/').strip('/') + '/'
    else:
        permalink = BASEURL + '/'
    
    return permalink


def resolve_relative_link(link_path: str, current_file: Path) -> str:
    """Resolve relative link to absolute permalink."""
    # Handle anchors
    anchor = ""
    if '#' in link_path:
        link_path, anchor = link_path.split('#', 1)
        anchor = f"#{anchor}"
    
    # Skip external links
    if '://' in link_path or link_path.startswith('mailto:'):
        return link_path + anchor
    
    # If already absolute with baseurl, return as is
    if link_path.startswith(BASEURL):
        return link_path.rstrip('/') + '/' + anchor
    
    # Remove .md extension
    if link_path.endswith('.md'):
        link_path = link_path[:-3]
    
    # Resolve relative path
    current_dir = current_file.parent
    
    # Handle relative paths
    if link_path.startswith('./'):
        link_path = link_path[2:]
    elif link_path.startswith('../'):
        # Calculate relative path
        parts = link_path.split('/')
        up_count = sum(1 for p in parts if p == '..')
        remaining = [p for p in parts if p and p != '..']
        
        target_dir = current_dir
        for _ in range(up_count):
            if target_dir == PROJECT_ROOT:
                break
            target_dir = target_dir.parent
        
        if remaining:
            target_file = target_dir / '/'.join(remaining)
        else:
            target_file = target_dir / 'index.md'
    else:
        # Direct relative path
        target_file = current_dir / link_path
    
    # Try to find the actual file
    possibilities = [
        target_file.with_suffix('.md'),
        target_file / 'index.md',
    ]
    
    for poss in possibilities:
        if poss.exists() and poss.is_file():
            return get_permalink_from_file(poss) + anchor
    
    # If file not found, try to construct permalink from path
    # This is a fallback
    rel_path = target_file.relative_to(PROJECT_ROOT) if target_file.is_relative_to(PROJECT_ROOT) else None
    if rel_path:
        path_str = str(rel_path).replace('.md', '')
        if path_str.endswith('/index') or path_str == 'index':
            path_str = path_str.replace('/index', '').replace('index', '')
        if path_str:
            return BASEURL + '/' + path_str.replace('\\', '/').strip('/') + '/' + anchor
    
    # Last resort: return original with baseurl
    clean_path = link_path.strip('/')
    return BASEURL + '/' + clean_path + '/' + anchor


def fix_links_in_file(file_path: Path) -> int:
    """Fix all links in a markdown file to use absolute permalinks."""
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
        
        # Skip if already absolute with baseurl
        if link_path.startswith(BASEURL):
            return match.group(0)
        
        # Convert to absolute permalink
        new_path = resolve_relative_link(link_path, file_path)
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
    print(f"Converting all links to absolute permalinks with baseurl '{BASEURL}'...\n")
    
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
    print(f"\nAll links are now absolute permalinks with baseurl")
    print(f"Format: {BASEURL}/section/path/to/page/")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

