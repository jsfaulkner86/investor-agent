from supabase import create_client, Client
from config.settings import settings

supabase: Client = create_client(settings.supabase_url, settings.supabase_key)

def upsert_investor(investor: dict) -> dict:
    """Insert or update an investor profile. Deduplicates by investor_id."""
    result = (
        supabase.table("investors")
        .upsert(investor, on_conflict="investor_id")
        .execute()
    )
    return result.data

def get_existing_investor_ids() -> list[str]:
    """Return all known investor IDs to avoid re-processing."""
    result = supabase.table("investors").select("investor_id").execute()
    return [row["investor_id"] for row in result.data]

def get_investors_by_min_score(min_score: int = 60) -> list[dict]:
    """Fetch investors at or above the fit score threshold."""
    result = (
        supabase.table("investors")
        .select("*")
        .gte("fit_score", min_score)
        .order("fit_score", desc=True)
        .execute()
    )
    return result.data
