from notion_client import Client
from config.settings import settings

notion = Client(auth=settings.notion_api_key)

def push_investor_to_notion(investor: dict) -> str:
    """
    Write an investor profile to the Notion CRM database.
    Returns the URL of the created/updated Notion page.
    """
    props = {
        "Name": {"title": [{"text": {"content": investor.get("name", "Unknown")}}]},
        "Type": {"select": {"name": investor.get("type", "Unknown")}},
        "Fit Score": {"number": investor.get("fit_score", 0)},
        "Fund Size": {"rich_text": [{"text": {"content": investor.get("fund_size", "Unknown")}}]},
        "Last Women's Health Investment": {"rich_text": [{"text": {"content": investor.get("last_investment", "Unknown")}}]},
        "Website": {"url": investor.get("website")},
        "LinkedIn": {"url": investor.get("linkedin")},
        "Stage Focus": {"rich_text": [{"text": {"content": investor.get("stage_focus", "Unknown")}}]},
        "Score Rationale": {"rich_text": [{"text": {"content": investor.get("score_rationale", "")}}]},
        "Status": {"select": {"name": "New"}},
    }
    page = notion.pages.create(
        parent={"database_id": settings.notion_database_id},
        properties=props,
    )
    return page["url"]
