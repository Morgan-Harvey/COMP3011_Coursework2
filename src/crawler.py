import requests, time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def extract_links(soup, base_url):
    soup = BeautifulSoup(soup, 'html.parser')
    links = set()
    
    for tag in soup.find_all('a', href=True):
        href = tag['href']
        full_url = urljoin(base_url, href)
        
        if urlparse(full_url).netloc == urlparse(base_url).netloc:
            links.add(full_url)
    
    return links

def crawl(base_url, delay=6):
    
    visited = set()
    queued = set([base_url])
    to_visit = [base_url]
    pages = {}
    
    while to_visit:
        url = to_visit.pop(0)
        
        if url in visited:
            continue
    
        try:
            time.sleep(delay)
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
        except requests.RequestException:
            print(f"Failed: {url}")
            continue
        
        visited.add(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for tag in soup(['script', 'style']):
            tag.decompose()
            
        pages[url] = soup.get_text()
        
        new_links = extract_links(soup, url)
        
        for link in new_links:
            if link not in visited and link not in queued:
                to_visit.append(link)
                queued.add(link)
        
    return pages