import resend
from config.settings import settings
from db.supabase_client import get_investors_by_min_score

resend.api_key = settings.resend_api_key

def build_investor_row(investor: dict) -> str:
    score_badge = f"<strong style='color:#2e7d32'>Score: {investor.get('fit_score', 'N/A')}/100</strong>"
    return f"""
    <tr style='border-bottom:1px solid #eee'>
      <td style='padding:12px'>
        <strong>{investor.get('name', 'Unknown')}</strong><br/>
        <em>{investor.get('type', '')} &mdash; {investor.get('stage_focus', '')}</em><br/>
        {score_badge}<br/>
        <small>{investor.get('score_rationale', '')}</small><br/>
        <a href='{investor.get('website', '#')}'>Website</a>
        {f"&nbsp;|&nbsp;<a href='{investor.get('linkedin')}'>LinkedIn</a>" if investor.get('linkedin') else ''}
      </td>
    </tr>
    """

def send_biweekly_digest(recipient_emails: list[str]):
    investors = get_investors_by_min_score(settings.min_fit_score)
    if not investors:
        print("No investors above threshold — skipping digest.")
        return

    rows = "".join(build_investor_row(inv) for inv in investors[:10])
    html_body = f"""
    <html><body style='font-family:sans-serif;max-width:700px;margin:auto'>
      <h2 style='color:#1a237e'>🏥 Women's Health Investor Intelligence</h2>
      <p style='color:#555'>Bi-weekly pipeline update from <strong>The Faulkner Group</strong></p>
      <table width='100%' cellpadding='0' cellspacing='0'>
        {rows}
      </table>
      <hr/>
      <p style='font-size:12px;color:#999'>Powered by Investor Agent &mdash; The Faulkner Group Advisors</p>
    </body></html>
    """

    for email in recipient_emails:
        resend.Emails.send({
            "from": settings.digest_from_email,
            "to": email,
            "subject": "Women's Health Investor Pipeline — Bi-Weekly Update",
            "html": html_body,
        })
        print(f"Digest sent to {email}")
