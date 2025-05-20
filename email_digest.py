import smtplib
from email.mime.text import MIMEText
from openai_module import summarize_insights

def send_gpt_email_summary(insight_text, email_user, email_pass, email_to, subject):
    try:
        summary = summarize_insights(insight_text)

        # Compose email
        msg = MIMEText(summary)
        msg["Subject"] = subject
        msg["From"] = email_user
        msg["To"] = email_to

        # Send email via SMTP (Gmail example)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email_user, email_pass)
            server.send_message(msg)

        return "✅ Email sent successfully."

    except Exception as e:
        return f"❌ Error sending email: {e}"
