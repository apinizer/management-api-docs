#!/usr/bin/env python3
"""
Smart comprehensive link fixer for Jekyll GitHub Pages.
- Finds all links in markdown files
- Resolves relative paths based on file location
- Verifies target files exist in filesystem
- Converts to proper Jekyll permalink format
- Handles incomplete paths and missing segments
- Fixes .md extensions
- Handles baseurl consideration
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


def get_permalink_from_file(file_path: Path) -> str:
    """
    Get Jekyll permalink from file path or front matter.
    Returns permalink in format: /section/path/to/page/
    """
    # Read front matter if exists
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for permalink in front matter
        permalink_match = re.search(r'permalink:\s*([^\n]+)', content)
        if permalink_match:
            permalink = permalink_match.group(1).strip().strip('"\'')
            if permalink.startswith('/'):
                return permalink.rstrip('/') + '/'
    except Exception:
        pass
    
    # Generate permalink from file path
    rel_path = file_path.relative_to(PROJECT_ROOT)
    
    # Remove .md extension
    path_str = str(rel_path).replace('.md', '')
    
    # Handle index files
    if path_str.endswith('/index') or path_str == 'index':
        path_str = path_str.replace('/index', '').replace('index', '')
    
    # Convert to permalink
    if path_str:
        permalink = '/' + path_str.replace('\\', '/').strip('/') + '/'
    else:
        permalink = '/'
    
    return permalink


def find_file_by_path(link_path: str, current_file: Path) -> Optional[Path]:
    """
    Find actual file path from a link path.
    Handles various path formats and searches filesystem.
    """
    # Handle anchors
    if '#' in link_path:
        link_path = link_path.split('#')[0]
    
    # Skip external links
    if '://' in link_path or link_path.startswith('mailto:'):
        return None
    
    # Remove .md extension if present
    original_path = link_path
    if link_path.endswith('.md'):
        link_path = link_path[:-3]
    
    current_dir = current_file.parent
    
    # Strategy 1: If absolute path starting with /
    if link_path.startswith('/'):
        # Remove leading slash
        path_parts = [p for p in link_path.strip('/').split('/') if p]
        
        # Try direct path
        if path_parts:
            potential_path = PROJECT_ROOT / '/'.join(path_parts)
            # Try with .md
            if potential_path.with_suffix('.md').exists():
                return potential_path.with_suffix('.md')
            # Try as directory with index.md
            if (potential_path / 'index.md').exists():
                return potential_path / 'index.md'
    
    # Strategy 2: Relative paths (./file, ../file, file)
    if not link_path.startswith('/') or link_path.startswith('./') or '../' in link_path:
        # Clean path
        clean_path = link_path.lstrip('./')
        
        # Handle ../ paths
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
                # Try various combinations
                possibilities = [
                    target_dir / '/'.join(remaining),
                    target_dir / '/'.join(remaining) + '.md',
                    target_dir / '/'.join(remaining) / 'index.md',
                ]
                
                for poss in possibilities:
                    if poss.exists() and poss.is_file():
                        return poss
        else:
            # Direct relative path
            possibilities = [
                current_dir / clean_path,
                current_dir / (clean_path + '.md'),
                current_dir / clean_path / 'index.md',
            ]
            
            for poss in possibilities:
                if poss.exists() and poss.is_file():
                    return poss
    
    # Strategy 3: Search by filename
    filename = link_path.split('/')[-1] if '/' in link_path else link_path
    if filename:
        # Search for files with this name
        for md_file in PROJECT_ROOT.rglob(f'{filename}.md'):
            if md_file.is_file():
                return md_file
        
        # Also try with index.md
        for md_file in PROJECT_ROOT.rglob(f'{filename}/index.md'):
            if md_file.is_file():
                return md_file
    
    # Strategy 4: Match path segments
    link_segments = [s for s in link_path.strip('/').split('/') if s]
    if link_segments:
        # Try to find file matching end segments
        for md_file in PROJECT_ROOT.rglob('*.md'):
            if md_file.is_file():
                rel_path = md_file.relative_to(PROJECT_ROOT)
                path_segments = [s for s in str(rel_path).replace('.md', '').split('/') if s]
                
                # Check if link segments match end of path segments
                if len(path_segments) >= len(link_segments):
                    if path_segments[-len(link_segments):] == link_segments:
                        return md_file
    
    return None


def fix_links_in_file(file_path: Path, file_permalinks: Dict[Path, str], all_files: Set[Path]) -> Tuple[int, int, list]:
    """
    Fix all links in a markdown file.
    
    Returns:
        Tuple of (links_fixed, links_not_found, warnings)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return (0, 0, [])
    
    original_content = content
    fixed_count = 0
    not_found_count = 0
    warnings = []
    
    def replace_link(match):
        nonlocal fixed_count, not_found_count
        link_text = match.group(1)
        link_path = match.group(2)
        
        # Handle anchors
        anchor = ""
        if '#' in link_path:
            link_path, anchor = link_path.split('#', 1)
            anchor = f"#{anchor}"
        
        # Skip external links
        if '://' in link_path or link_path.startswith('mailto:'):
            return match.group(0)
        
        # Find the target file
        target_file = find_file_by_path(link_path, file_path)
        
        if target_file and target_file.exists() and target_file in all_files:
            # Get permalink for target file
            if target_file in file_permalinks:
                new_permalink = file_permalinks[target_file]
            else:
                new_permalink = get_permalink_from_file(target_file)
                file_permalinks[target_file] = new_permalink
            
            new_link = f'[{link_text}]({new_permalink}{anchor})'
            
            # Only count as fixed if it changed
            if match.group(0) != new_link:
                fixed_count += 1
            
            return new_link
        else:
            # File not found - try to create a reasonable permalink
            not_found_count += 1
            
            # Clean up the path
            clean_path = link_path.strip('/')
            if clean_path.endswith('.md'):
                clean_path = clean_path[:-3]
            
            # Remove duplicate segments
            segments = [s for s in clean_path.split('/') if s]
            seen = set()
            unique_segments = []
            for seg in segments:
                if seg not in seen:
                    unique_segments.append(seg)
                    seen.add(seg)
                elif seg in SECTION_PREFIXES:
                    # Reset on section prefix
                    unique_segments = [seg]
                    seen = {seg}
            
            new_path = '/' + '/'.join(unique_segments) + '/' if unique_segments else '/'
            
            new_link = f'[{link_text}]({new_path}{anchor})'
            
            warnings.append(f"Link '{link_path}' not found, guessed: {new_path}")
            
            if match.group(0) != new_link:
                fixed_count += 1
            
            return new_link
    
    # Replace all markdown links
    content = re.sub(LINK_PATTERN, replace_link, content)
    
    # Write if changed
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return (fixed_count, not_found_count, warnings)
        except Exception as e:
            print(f"❌ Error writing {file_path}: {e}")
            return (0, 0, [])
    
    return (0, 0, [])


def build_file_set() -> Set[Path]:
    """Build set of all markdown files in project."""
    files = set()
    for md_file in PROJECT_ROOT.rglob('*.md'):
        if md_file.is_file() and not any(part.startswith('.') for part in md_file.parts):
            if md_file.name not in ['SESSION_SUMMARY.md']:
                files.add(md_file)
    # Also include README.md explicitly
    readme_path = PROJECT_ROOT / 'README.md'
    if readme_path.exists():
        files.add(readme_path)
    return files


def build_permalink_cache(files: Set[Path]) -> Dict[Path, str]:
    """Build a cache of file paths to permalinks."""
    cache = {}
    for md_file in files:
        cache[md_file] = get_permalink_from_file(md_file)
    return cache


def main():
    """Main function."""
    print("Building file index...")
    all_files = build_file_set()
    print(f"✓ Found {len(all_files)} markdown files\n")
    
    print("Building permalink cache...")
    file_permalinks = build_permalink_cache(all_files)
    print(f"✓ Cached {len(file_permalinks)} permalinks\n")
    
    print("Fixing links in all markdown files...\n")
    
    total_files = 0
    total_fixed = 0
    total_not_found = 0
    all_warnings = []
    
    # Process all markdown files
    for md_file in sorted(all_files):
        total_files += 1
        fixed, not_found, warnings = fix_links_in_file(md_file, file_permalinks, all_files)
        total_fixed += fixed
        total_not_found += not_found
        all_warnings.extend([f"{md_file.relative_to(PROJECT_ROOT)}: {w}" for w in warnings])
        
        if fixed > 0 or not_found > 0:
            status = f"✓ Fixed {fixed}"
            if not_found > 0:
                status += f", {not_found} not found"
            print(f"{status} links in {md_file.relative_to(PROJECT_ROOT)}")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files processed: {total_files}")
    print(f"  Links fixed: {total_fixed}")
    print(f"  Links not found (guessed): {total_not_found}")
    
    if all_warnings:
        print(f"\n⚠️  Warnings ({len(all_warnings)}):")
        for warning in all_warnings[:10]:  # Show first 10
            print(f"  - {warning}")
        if len(all_warnings) > 10:
            print(f"  ... and {len(all_warnings) - 10} more")
    
    print(f"{'='*60}")


if __name__ == '__main__':
    main()

