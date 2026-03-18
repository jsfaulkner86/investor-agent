from crewai import Agent

SCORING_RUBRIC = """
Score each investor 0-100 on fit for women's health tech companies:

- Women's health portfolio depth (0-30 pts): number and recency of women's health investments
- Stage alignment (0-20 pts): invests at Seed, Series A, B — not just late stage
- Check size range (0-20 pts): relevant to early/growth stage health tech
- Founder accessibility (0-15 pts): angel or small fund vs. inaccessible mega-fund
- Geographic relevance (0-15 pts): US-focused or global with US portfolio presence

Return a numeric score and a 1-sentence rationale.
"""

scoring_agent = Agent(
    role="Investor Fit Scorer",
    goal=(
        "Evaluate each enriched investor profile against a structured rubric and assign "
        "a fit score (0-100) for women's health tech founders seeking capital."
    ),
    backstory=(
        "You are a capital markets strategist with deep expertise in women's health funding. "
        "You score investors objectively so founders can prioritize their outreach effort."
    ),
    tools=[],
    verbose=True,
    allow_delegation=False,
)

SCORING_PROMPT = SCORING_RUBRIC
