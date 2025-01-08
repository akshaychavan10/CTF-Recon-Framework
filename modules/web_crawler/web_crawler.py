import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from config import PROJECTS_DIR

def is_valid_url(url):
    """
    Check if a URL is valid.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    """
    Extract all links from a webpage.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            full_url = urljoin(url, href)
            if is_valid_url(full_url):
                links.add(full_url)
        return links
    except Exception as e:
        print(f"[-] Error fetching {url}: {e}")
        return set()

def crawl_website(start_url, max_depth=2):
    """
    Crawl a website starting from the given URL.
    """
    visited = set()
    to_visit = [(start_url, 0)]  # (url, depth)
    all_links = set()

    while to_visit:
        url, depth = to_visit.pop(0)
        if url in visited or depth > max_depth:
            continue

        print(f"[+] Crawling: {url} (Depth: {depth})")
        visited.add(url)
        links = get_all_links(url)
        all_links.update(links)

        for link in links:
            if link not in visited:
                to_visit.append((link, depth + 1))

    return all_links

def save_crawl_results(project_name, domain, links):
    """
    Save the crawled links to a file.
    """
    output_dir = os.path.join(PROJECTS_DIR, project_name, "web_crawling")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate a timestamp for the filename
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = os.path.join(output_dir, f"{current_time}_{domain}_crawl_results.txt")

    # Save the links to the file
    with open(output_file, "w") as f:
        for link in links:
            f.write(f"{link}\n")

    print(f"[+] Crawl results saved to {output_file}")

def web_crawl(project_name, domain):
    """
    Perform web crawling for the given domain.
    """
    start_url = f"http://{domain}"  # Start with HTTP
    print(f"[+] Starting web crawl for {start_url}...")

    # Crawl the website
    links = crawl_website(start_url, max_depth=2)

    # Save the results
    save_crawl_results(project_name, domain, links)