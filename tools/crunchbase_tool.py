import httpx
from config.settings import settings

CRUNCHBASE_BASE = "https://api.crunchbase.com/api/v4"

def search_organizations(keywords: list[str], investor_types: list[str] = None) -> list[dict]:
    """
    Search Crunchbase for investor organizations by keyword + investor type.
    Returns a list of raw organization records.
    """
    investor_types = investor_types or ["venture_capital", "private_equity", "angel"]
    params = {
        "user_key": settings.crunchbase_api_key,
        "name": " ".join(keywords),
        "organization_types": ",".join(investor_types),
    }
    response = httpx.get(
        f"{CRUNCHBASE_BASE}/searches/organizations",
        params=params,
        timeout=20,
    )
    response.raise_for_status()
    return response.json().get("entities", [])

def get_organization_details(org_identifier: str) -> dict:
    """Fetch full profile for a specific Crunchbase org."""
    params = {"user_key": settings.crunchbase_api_key}
    response = httpx.get(
        f"{CRUNCHBASE_BASE}/entities/organizations/{org_identifier}",
        params=params,
        timeout=20,
    )
    response.raise_for_status()
    return response.json().get("properties", {})
