import httpx
from bs4 import BeautifulSoup

def scrape_page_text(url: str) -> str:
    """Scrape visible text from a web page. Used as fallback research tool."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; InvestorAgent/1.0)"}
    response = httpx.get(url, headers=headers, timeout=15, follow_redirects=True)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    return " ".join(soup.get_text(separator=" ").split())
