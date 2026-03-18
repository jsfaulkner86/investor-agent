from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pipelines.biweekly_digest import run_pipeline
from config.settings import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("InvestorAgentScheduler")

scheduler = BlockingScheduler()

scheduler.add_job(
    func=run_pipeline,
    trigger=IntervalTrigger(days=settings.run_cadence_days),
    id="biweekly_investor_pipeline",
    name="Bi-Weekly Women's Health Investor Pipeline",
    replace_existing=True,
)

if __name__ == "__main__":
    logger.info(f"Scheduler starting — running every {settings.run_cadence_days} days.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped.")
