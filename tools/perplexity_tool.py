import httpx
from config.settings import settings

PERPLEXITY_URL = "https://api.perplexity.ai/chat/completions"

def search_investors(query: str) -> str:
    """
    Use Perplexity Sonar to research investors in women's health.
    Returns a raw text response for the enrichment agent to parse.
    """
    headers = {
        "Authorization": f"Bearer {settings.perplexity_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an expert investor researcher focused exclusively on women's health. "
                    "Return structured investor profiles including: firm name, type (VC/PE/angel/family office), "
                    "fund size if known, portfolio focus, last known women's health investment, "
                    "founding partner names, website, and LinkedIn if available."
                ),
            },
            {"role": "user", "content": query},
        ],
    }
    response = httpx.post(PERPLEXITY_URL, json=payload, headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
