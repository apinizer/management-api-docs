#!/usr/bin/env python3
"""
Comprehensive link fixer for Jekyll GitHub Pages.
This script:
1. Finds all links in markdown files
2. Resolves relative paths based on file location
3. Verifies target files exist in filesystem
4. Converts to proper Jekyll permalink format
5. Fixes wrong path segments
6. Handles incomplete paths and missing segments
7. Removes .md extensions
8. Fixes double slashes
9. Removes duplicate path segments

Usage: python3 fix_all_links.py
"""

import os
import re
from pathlib import Path
from typing import Dict, Optional, Tuple, Set

PROJECT_ROOT = Path(__file__).parent

# Pattern to match markdown links: [text](path) or [text](path#anchor)
LINK_PATTERN = r'\[([^\]]+)\]\(([^\)]+)\)'

# Section prefixes for Jekyll
SECTION_PREFIXES = ['01-getting-started', '02-api-reference', '03-appendix']

# Common wrong path patterns and their corrections
PATH_FIXES = [
    (r'/02-api-reference/01-getting-started/', '/01-getting-started/'),
    (r'/02-api-reference/01-getting-started', '/01-getting-started/'),
    (r'/03-appendix/01-getting-started/', '/01-getting-started/'),
    (r'/03-appendix/01-getting-started', '/01-getting-started/'),
    (r'/02-api-reference/04-api-proxies/05-policies/', '/02-api-reference/05-policies/'),
    (r'/02-api-reference/04-api-proxies/05-policies', '/02-api-reference/05-policies/'),
    (r'/02-api-reference/04-api-proxies/06-connections/', '/02-api-reference/06-connections/'),
    (r'/02-api-reference/04-api-proxies/06-connections', '/02-api-reference/06-connections/'),
    (r'/02-api-reference/04-api-proxies/07-credentials/', '/02-api-reference/07-credentials/'),
    (r'/02-api-reference/04-api-proxies/07-credentials', '/02-api-reference/07-credentials/'),
    (r'/02-api-reference/04-api-proxies/08-certificates/', '/02-api-reference/08-certificates/'),
    (r'/02-api-reference/04-api-proxies/08-certificates', '/02-api-reference/08-certificates/'),
    (r'/03-appendix/02-api-reference/', '/02-api-reference/'),
    (r'/03-appendix/02-api-reference', '/02-api-reference/'),
    (r'/02-api-reference/01-getting-started/([^)]+)', r'/01-getting-started/\1'),
    (r'/03-appendix/01-getting-started/([^)]+)', r'/01-getting-started/\1'),
    (r'/02-api-reference/04-api-proxies/05-policies/([^)]+)', r'/02-api-reference/05-policies/\1'),
    (r'/02-api-reference/04-api-proxies/06-connections/([^)]+)', r'/02-api-reference/06-connections/\1'),
    (r'/02-api-reference/04-api-proxies/07-credentials/([^)]+)', r'/02-api-reference/07-credentials/\1'),
    (r'/02-api-reference/04-api-proxies/08-certificates/([^)]+)', r'/02-api-reference/08-certificates/\1'),
    (r'/03-appendix/02-api-reference/([^)]+)', r'/02-api-reference/\1'),
]


def get_permalink_from_file(file_path: Path) -> str:
    """Get Jekyll permalink from file path or front matter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        permalink_match = re.search(r'permalink:\s*([^\n]+)', content)
        if permalink_match:
            permalink = permalink_match.group(1).strip().strip('"\'')
            if permalink.startswith('/'):
                return permalink.rstrip('/') + '/'
    except Exception:
        pass
    
    rel_path = file_path.relative_to(PROJECT_ROOT)
    path_str = str(rel_path).replace('.md', '')
    
    if path_str.endswith('/index') or path_str == 'index':
        path_str = path_str.replace('/index', '').replace('index', '')
    
    if path_str:
        permalink = '/' + path_str.replace('\\', '/').strip('/') + '/'
    else:
        permalink = '/'
    
    return permalink


def find_file_by_path(link_path: str, current_file: Path) -> Optional[Path]:
    """Find actual file path from a link path."""
    if '#' in link_path:
        link_path = link_path.split('#')[0]
    
    if '://' in link_path or link_path.startswith('mailto:'):
        return None
    
    if link_path.endswith('.md'):
        link_path = link_path[:-3]
    
    current_dir = current_file.parent
    
    # Absolute path
    if link_path.startswith('/'):
        path_parts = [p for p in link_path.strip('/').split('/') if p]
        if path_parts:
            potential_path = PROJECT_ROOT / '/'.join(path_parts)
            if potential_path.with_suffix('.md').exists():
                return potential_path.with_suffix('.md')
            if (potential_path / 'index.md').exists():
                return potential_path / 'index.md'
    
    # Relative paths
    if not link_path.startswith('/') or link_path.startswith('./') or '../' in link_path:
        clean_path = link_path.lstrip('./')
        
        if '../' in clean_path:
            parts = clean_path.split('/')
            up_count = sum(1 for p in parts if p == '..')
            remaining = [p for p in parts if p and p != '..']
            
            target_dir = current_dir
            for _ in range(up_count):
                if target_dir == PROJECT_ROOT:
                    break
                target_dir = target_dir.parent
            
            if remaining:
                possibilities = [
                    target_dir / '/'.join(remaining),
                    target_dir / '/'.join(remaining) + '.md',
                    target_dir / '/'.join(remaining) / 'index.md',
                ]
                for poss in possibilities:
                    if poss.exists() and poss.is_file():
                        return poss
        else:
            possibilities = [
                current_dir / clean_path,
                current_dir / (clean_path + '.md'),
                current_dir / clean_path / 'index.md',
            ]
            for poss in possibilities:
                if poss.exists() and poss.is_file():
                    return poss
    
    # Search by filename
    filename = link_path.split('/')[-1] if '/' in link_path else link_path
    if filename:
        for md_file in PROJECT_ROOT.rglob(f'{filename}.md'):
            if md_file.is_file():
                return md_file
        for md_file in PROJECT_ROOT.rglob(f'{filename}/index.md'):
            if md_file.is_file():
                return md_file
    
    # Match path segments
    link_segments = [s for s in link_path.strip('/').split('/') if s]
    if link_segments:
        for md_file in PROJECT_ROOT.rglob('*.md'):
            if md_file.is_file():
                rel_path = md_file.relative_to(PROJECT_ROOT)
                path_segments = [s for s in str(rel_path).replace('.md', '').split('/') if s]
                if len(path_segments) >= len(link_segments):
                    if path_segments[-len(link_segments):] == link_segments:
                        return md_file
    
    return None


def clean_path(path: str) -> str:
    """Clean path: remove double slashes, duplicate segments, etc."""
    # Remove double slashes
    while '//' in path:
        path = path.replace('//', '/')
    
    # Remove duplicate consecutive segments
    segments = [s for s in path.split('/') if s]
    seen = set()
    unique_segments = []
    for seg in segments:
        if seg not in seen:
            unique_segments.append(seg)
            seen.add(seg)
        elif seg in SECTION_PREFIXES:
            unique_segments = [seg]
            seen = {seg}
    
    return '/' + '/'.join(unique_segments) + '/' if unique_segments else '/'


def fix_path_in_link(link_path: str) -> str:
    """Fix wrong path segments in a link path."""
    anchor = ""
    if '#' in link_path:
        link_path, anchor = link_path.split('#', 1)
        anchor = f"#{anchor}"
    
    # Apply path fixes
    for wrong_pattern, correct_pattern in PATH_FIXES:
        link_path = re.sub(wrong_pattern, correct_pattern, link_path)
    
    # Clean path
    link_path = clean_path(link_path)
    
    # Ensure ends with / if it's a path (not external)
    if link_path.startswith('/') and not link_path.endswith('/') and '://' not in link_path:
        link_path = link_path + '/'
    
    return link_path + anchor


def fix_links_in_file(file_path: Path, file_permalinks: Dict[Path, str], all_files: Set[Path]) -> Tuple[int, int]:
    """Fix all links in a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return (0, 0)
    
    original_content = content
    fixed_count = 0
    not_found_count = 0
    
    def replace_link(match):
        nonlocal fixed_count, not_found_count
        link_text = match.group(1)
        link_path = match.group(2)
        
        anchor = ""
        if '#' in link_path:
            link_path, anchor = link_path.split('#', 1)
            anchor = f"#{anchor}"
        
        if '://' in link_path or link_path.startswith('mailto:'):
            return match.group(0)
        
        # First, try to find the actual file
        target_file = find_file_by_path(link_path, file_path)
        
        if target_file and target_file.exists() and target_file in all_files:
            if target_file in file_permalinks:
                new_permalink = file_permalinks[target_file]
            else:
                new_permalink = get_permalink_from_file(target_file)
                file_permalinks[target_file] = new_permalink
            
            new_link = f'[{link_text}]({new_permalink}{anchor})'
            
            if match.group(0) != new_link:
                fixed_count += 1
            
            return new_link
        else:
            # File not found - fix path anyway
            not_found_count += 1
            
            clean_path_str = link_path.strip('/')
            if clean_path_str.endswith('.md'):
                clean_path_str = clean_path_str[:-3]
            
            new_path = fix_path_in_link('/' + clean_path_str if clean_path_str else '/')
            new_link = f'[{link_text}]({new_path}{anchor})'
            
            if match.group(0) != new_link:
                fixed_count += 1
            
            return new_link
    
    content = re.sub(LINK_PATTERN, replace_link, content)
    
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return (fixed_count, not_found_count)
        except Exception as e:
            print(f"❌ Error writing {file_path}: {e}")
            return (0, 0)
    
    return (0, 0)


def build_file_set() -> Set[Path]:
    """Build set of all markdown files in project."""
    files = set()
    for md_file in PROJECT_ROOT.rglob('*.md'):
        if md_file.is_file() and not any(part.startswith('.') for part in md_file.parts):
            if md_file.name not in ['SESSION_SUMMARY.md']:
                files.add(md_file)
    readme_path = PROJECT_ROOT / 'README.md'
    if readme_path.exists():
        files.add(readme_path)
    return files


def main():
    """Main function."""
    print("="*60)
    print("Comprehensive Link Fixer for Jekyll GitHub Pages")
    print("="*60)
    print("\nBuilding file index...")
    all_files = build_file_set()
    print(f"✓ Found {len(all_files)} markdown files\n")
    
    print("Building permalink cache...")
    file_permalinks = {}
    for md_file in all_files:
        file_permalinks[md_file] = get_permalink_from_file(md_file)
    print(f"✓ Cached {len(file_permalinks)} permalinks\n")
    
    print("Fixing links in all markdown files...\n")
    
    total_files = 0
    total_fixed = 0
    total_not_found = 0
    
    for md_file in sorted(all_files):
        total_files += 1
        fixed, not_found = fix_links_in_file(md_file, file_permalinks, all_files)
        total_fixed += fixed
        total_not_found += not_found
        
        if fixed > 0 or not_found > 0:
            status = f"✓ Fixed {fixed}"
            if not_found > 0:
                status += f", {not_found} guessed"
            print(f"{status} links in {md_file.relative_to(PROJECT_ROOT)}")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files processed: {total_files}")
    print(f"  Links fixed: {total_fixed}")
    print(f"  Links not found (guessed): {total_not_found}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

