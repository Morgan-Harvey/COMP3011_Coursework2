from bs4 import BeautifulSoup
from src.crawler import extract_links

def test_extract_links_same_domain():
    html = """
        <a href="/page1">Page 1</a>
        <a href="https://quotes.toscrape.com/page/2/">Page 2</a>
        <a href="https://google.com">External</a>
    """
    soup = BeautifulSoup(html, "html.parser")

    links = extract_links(soup, "https://quotes.toscrape.com")

    assert "https://quotes.toscrape.com/page1" in links
    assert "https://quotes.toscrape.com/page/2/" in links
    assert "https://google.com" not in links


def test_extract_links_no_duplicates():
    html = """
        <a href="/page1">A</a>
        <a href="/page1">B</a>
    """
    soup = BeautifulSoup(html, "html.parser")

    links = extract_links(soup, "https://quotes.toscrape.com")

    assert len(links) == 1


def test_extract_links_no_anchors():
    html = "<html><body><p>No links here</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")

    links = extract_links(soup, "https://quotes.toscrape.com")

    assert links == set()


def test_extract_links_anchor_without_href():
    html = """
        <a>Missing href</a>
        <a href="/valid">Valid</a>
    """
    soup = BeautifulSoup(html, "html.parser")

    links = extract_links(soup, "https://quotes.toscrape.com")

    assert "https://quotes.toscrape.com/valid" in links
    assert len(links) == 1