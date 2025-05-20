import smtplib
from email.mime.text import MIMEText
from openai_module import summarize_insights

def send_gpt_email_summary(insight_text, email_user, email_pass, email_to, subject):
    """
    Sends a GPT-generated summary of campaign insights to a recipient via SMTP email.
    Args:
        insight_text (str): The raw campaign metrics or performance data.
        email_user (str): Sender's email address.
        email_pass (str): Sender's email app password.
        email_to (str): Recipient email address.
        subject (str): Email subject line.

    Returns:
        str: Status message indicating success or failure.
    """
    try:
        # Step 1: Summarize insight via OpenAI
        summary = summarize_insights(insight_text)

        # Step 2: Create email message
        msg = MIMEText(summary, "plain")
        msg["Subject"] = subject
        msg["From"] = email_user
        msg["To"] = email_to

        # Step 3: Send securely via Gmail SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email_user, email_pass)
            server.send_message(msg)

        return "✅ Email sent successfully."

    except smtplib.SMTPAuthenticationError:
        return "❌ Authentication failed. Check your SMTP email/password or enable app passwords."
    except smtplib.SMTPConnectError:
        return "❌ Failed to connect to the email server."
    except Exception as e:
        return f"❌ Error sending email: {str(e)}"
