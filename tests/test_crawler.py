from src.crawler import extract_links

def test_extract_links_same_domain():
    """Links to the same domain should be kept and resolved to absolute URLs."""
    html = """
        <a href="/page1">Page 1</a>
        <a href="https://quotes.toscrape.com/page/2/">Page 2</a>
        <a href="https://google.com">External</a>
    """
    links = extract_links(html, "https://quotes.toscrape.com")
    assert "https://quotes.toscrape.com/page1" in links
    assert "https://quotes.toscrape.com/page/2/" in links
    assert "https://google.com" not in links


def test_extract_links_no_duplicates():
    html = """
    <a href="/page1">A</a>
    <a href="/page1">B</a>
    """
    
    links = extract_links(html, "https://quotes.toscrape.com")
    
    assert len(links) == 1

def test_extract_links_no_anchors():
    """A page with no <a> tags should return empty without crashing."""
    
    html = "<html><body><p>No links here</p></body></html>"
    
    links = extract_links(html, "https://quotes.toscrape.com")
    
    assert links == set()


def test_extract_links_anchor_without_href():
    """<a> tags without href should be skipped, not crash."""
    
    html = """
    <a>Missing href</a>
    <a href="/valid">Valid</a>
    """
    
    links = extract_links(html, "https://quotes.toscrape.com")
    
    assert "https://quotes.toscrape.com/valid" in links
    assert len(links) == 1
