from crewai import Crew, Task
from agents.researcher_agent import researcher, RESEARCH_QUERIES
from agents.enrichment_agent import enrichment_agent
from agents.scoring_agent import scoring_agent, SCORING_PROMPT
from db.supabase_client import upsert_investor, get_existing_investor_ids
from delivery.notion_push import push_investor_to_notion
from delivery.email_digest import send_biweekly_digest
import json

# Configure your advisory client recipient list here
CLIENT_RECIPIENTS = [
    # "founder@womenshealthco.com",
]

def run_pipeline():
    print("[InvestorAgent] Starting bi-weekly pipeline run...")
    existing_ids = get_existing_investor_ids()

    for query in RESEARCH_QUERIES:
        research_task = Task(
            description=f"Research women's health investors using query: '{query}'",
            agent=researcher,
            expected_output="A list of investor names, types, and basic details.",
        )
        enrichment_task = Task(
            description="Enrich each discovered investor with full profile details.",
            agent=enrichment_agent,
            expected_output="A JSON array of enriched investor profiles.",
        )
        scoring_task = Task(
            description=f"Score each enriched investor profile using this rubric:\n{SCORING_PROMPT}",
            agent=scoring_agent,
            expected_output="Each investor profile with a fit_score (0-100) and score_rationale added.",
        )

        crew = Crew(
            agents=[researcher, enrichment_agent, scoring_agent],
            tasks=[research_task, enrichment_task, scoring_task],
            verbose=True,
        )
        result = crew.kickoff()

        # Parse result and persist
        try:
            investors = json.loads(result) if isinstance(result, str) else result
            for inv in investors:
                if inv.get("investor_id") not in existing_ids:
                    upsert_investor(inv)
                    push_investor_to_notion(inv)
        except Exception as e:
            print(f"[InvestorAgent] Parse/persist error: {e}")

    send_biweekly_digest(CLIENT_RECIPIENTS)
    print("[InvestorAgent] Pipeline run complete.")

if __name__ == "__main__":
    run_pipeline()
