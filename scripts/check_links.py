#!/usr/bin/env python3
"""
Broken Link Checker for Shows in AZ

This script checks for broken links in event files and validates venue URLs.
It can check both internal links and external venue URLs.
"""

import os
import sys
import re
import glob
import time
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Tuple, Set
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    print("Error: requests library is required. Install with: pip install requests")
    sys.exit(1)

class LinkChecker:
    def __init__(self, base_url: str = "https://showsinaz.com", timeout: int = 10, max_workers: int = 10):
        self.base_url = base_url
        self.timeout = timeout
        self.max_workers = max_workers
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
        })
        self.checked_urls: Dict[str, bool] = {}
        
    def extract_venue_urls_from_files(self, pattern: str = "content/**/*.md") -> List[Tuple[str, str, str]]:
        """Extract venue URLs from markdown files"""
        venue_urls = []
        
        for file_path in glob.glob(pattern, recursive=True):
            if os.path.basename(file_path) in ['_index.md']:
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract venue_url from frontmatter
                venue_url_match = re.search(r'^venue_url = "([^"]*)"', content, re.MULTILINE)
                if venue_url_match:
                    url = venue_url_match.group(1)
                    if url:  # Skip empty URLs
                        venue_urls.append((file_path, url, "venue_url"))
                        
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                
        return venue_urls
    
    def extract_content_links(self, pattern: str = "content/**/*.md") -> List[Tuple[str, str, str]]:
        """Extract links from markdown content"""
        content_links = []
        
        for file_path in glob.glob(pattern, recursive=True):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find markdown links [text](url)
                markdown_links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', content)
                for text, url in markdown_links:
                    if url.startswith(('http://', 'https://', '/')):
                        content_links.append((file_path, url, f"markdown_link: {text}"))
                
                # Find plain HTTP URLs
                url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+[^\s<>"{}|\\^`\[\].,;:]'
                plain_urls = re.findall(url_pattern, content)
                for url in plain_urls:
                    # Skip if it's already captured as a markdown link
                    if not any(url in link[1] for link in markdown_links):
                        content_links.append((file_path, url, "plain_url"))
                        
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                
        return content_links
    
    def check_url(self, url: str) -> Tuple[str, bool, str, int]:
        """Check if a URL is accessible"""
        if url in self.checked_urls:
            return url, self.checked_urls[url], "cached", 0
            
        try:
            # Handle relative URLs
            if url.startswith('/'):
                url = urljoin(self.base_url, url)
            
            response = self.session.head(url, timeout=self.timeout, allow_redirects=True)
            
            # Some servers don't support HEAD, try GET
            if response.status_code == 405:
                response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
                
            is_ok = response.status_code < 400
            self.checked_urls[url] = is_ok
            
            return url, is_ok, response.reason or "OK", response.status_code
            
        except requests.exceptions.Timeout:
            self.checked_urls[url] = False
            return url, False, "Timeout", 0
        except requests.exceptions.ConnectionError:
            self.checked_urls[url] = False
            return url, False, "Connection Error", 0
        except requests.exceptions.RequestException as e:
            self.checked_urls[url] = False
            return url, False, str(e), 0
        except Exception as e:
            self.checked_urls[url] = False
            return url, False, f"Unknown error: {e}", 0
    
    def check_links_batch(self, links: List[Tuple[str, str, str]]) -> List[Dict]:
        """Check multiple links concurrently"""
        results = []
        unique_urls = list(set(link[1] for link in links))
        
        print(f"Checking {len(unique_urls)} unique URLs...")
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all URL checks
            url_futures = {executor.submit(self.check_url, url): url for url in unique_urls}
            
            # Process results as they complete
            for future in as_completed(url_futures):
                url, is_ok, reason, status_code = future.result()
                
                # Find all files that reference this URL
                for file_path, link_url, link_type in links:
                    if link_url == url:
                        results.append({
                            'file': file_path,
                            'url': url,
                            'type': link_type,
                            'ok': is_ok,
                            'reason': reason,
                            'status_code': status_code
                        })
                        
                # Add a small delay to be nice to servers
                time.sleep(0.1)
        
        return results
    
    def generate_report(self, results: List[Dict]) -> Tuple[int, int]:
        """Generate a report of broken links"""
        broken_links = [r for r in results if not r['ok']]
        working_links = [r for r in results if r['ok']]
        
        print(f"\n=== LINK CHECK REPORT ===")
        print(f"Total links checked: {len(results)}")
        print(f"Working links: {len(working_links)}")
        print(f"Broken links: {len(broken_links)}")
        
        if broken_links:
            print(f"\n❌ BROKEN LINKS FOUND:")
            print("-" * 80)
            
            # Group by URL to avoid duplicates in output
            broken_by_url = {}
            for link in broken_links:
                url = link['url']
                if url not in broken_by_url:
                    broken_by_url[url] = []
                broken_by_url[url].append(link)
            
            for url, link_list in broken_by_url.items():
                first_link = link_list[0]
                file_count = len(link_list)
                files_text = f"({file_count} files)" if file_count > 1 else f"({first_link['file']})"
                
                print(f"🔗 {url}")
                print(f"   Status: {first_link['status_code']} - {first_link['reason']}")
                print(f"   Found in: {files_text}")
                if file_count > 1:
                    for link in link_list[:3]:  # Show first 3 files
                        print(f"     - {link['file']} ({link['type']})")
                    if file_count > 3:
                        print(f"     ... and {file_count - 3} more files")
                else:
                    print(f"     Type: {first_link['type']}")
                print()
        else:
            print(f"\n✅ All links are working!")
            
        return len(working_links), len(broken_links)

def main():
    parser = argparse.ArgumentParser(description='Check for broken links in Shows in AZ')
    parser.add_argument('--venue-urls-only', action='store_true', 
                       help='Only check venue URLs from frontmatter')
    parser.add_argument('--content-links-only', action='store_true',
                       help='Only check links in markdown content')
    parser.add_argument('--timeout', type=int, default=10,
                       help='Request timeout in seconds (default: 10)')
    parser.add_argument('--max-workers', type=int, default=10,
                       help='Maximum concurrent requests (default: 10)')
    parser.add_argument('--pattern', default='content/**/*.md',
                       help='File pattern to check (default: content/**/*.md)')
    
    args = parser.parse_args()
    
    checker = LinkChecker(timeout=args.timeout, max_workers=args.max_workers)
    all_links = []
    
    if not args.content_links_only:
        print("Extracting venue URLs...")
        venue_urls = checker.extract_venue_urls_from_files(args.pattern)
        all_links.extend(venue_urls)
        print(f"Found {len(venue_urls)} venue URLs")
    
    if not args.venue_urls_only:
        print("Extracting content links...")
        content_links = checker.extract_content_links(args.pattern)
        all_links.extend(content_links)
        print(f"Found {len(content_links)} content links")
    
    if not all_links:
        print("No links found to check.")
        return 0
    
    # Check all links
    results = checker.check_links_batch(all_links)
    
    # Generate report
    working_count, broken_count = checker.generate_report(results)
    
    # Return appropriate exit code
    return 1 if broken_count > 0 else 0

if __name__ == "__main__":
    sys.exit(main())