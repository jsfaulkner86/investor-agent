from crewai import Agent
from tools.perplexity_tool import search_investors
from tools.crunchbase_tool import search_organizations

RESEARCH_QUERIES = [
    "venture capital firms investing in women's health 2025 2026",
    "private equity women's health portfolio companies",
    "angel investors focused on femtech and women's health startups",
    "family offices investing women's health innovation",
    "corporate strategic investors women's health acquisitions",
    "new funds launched women's health femtech 2025 2026",
]

researcher = Agent(
    role="Women's Health Investor Researcher",
    goal=(
        "Discover new investors — VCs, PE firms, angels, family offices, and strategics — "
        "actively investing in women's health and femtech. Surface investors not yet in the database."
    ),
    backstory=(
        "You are a specialist investor researcher for The Faulkner Group, supporting women's health "
        "tech founders with ongoing pipeline intelligence. You are relentless, thorough, and focused "
        "exclusively on investors with a demonstrated interest in women's health."
    ),
    tools=[search_investors, search_organizations],
    verbose=True,
    allow_delegation=False,
)
