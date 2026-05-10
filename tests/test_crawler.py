from src.crawler import crawl, extract_links


def test_extract_links_same_domain():
    html = """
    <a href="/page1">Page 1</a>
    <a href="https://quotes.toscrape.com/page/2/">Page 2</a>
    <a href="https://google.com">External</a>
    """
    
    links = extract_links(html, "https://quotes.toscrape.com")
    
    assert "https://quotes.toscrape.com/page1" in links
    assert "https://quotes.toscrape.com/page/2/" in links
    assert "https://google.com" not in links
    
def test_crawl_page_content():
    pages = crawl("https://quotes.toscrape.com/", delay=0)
    
    for url, content in pages.items():
        assert isinstance(content, str)
        assert len(content) > 0
        
def test_extract_links_no_duplicates():
    html = """
    <a href="/page1">A</a>
    <a href="/page1">B</a>
    """
    
    links = extract_links(html, "https://quotes.toscrape.com")
    
    assert len(links) == 1
    
def test_no_duplicate_pages():
    pages = crawl("https://quotes.toscrape.com/", delay=0)
    
    urls = list(pages.keys())
    
    assert len(urls) == len(set(urls))