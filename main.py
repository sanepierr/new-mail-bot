import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from utils import get_headlines, format_email
from dotenv import load_dotenv

load_dotenv()

def send_email():
    api_key = os.getenv("SENDGRID_API_KEY")
    sender = os.getenv("SENDER_EMAIL")
    recipients = os.getenv("RECIPIENT_EMAILS").split(',')

    headlines = get_headlines()
    content = format_email(headlines)

    message = Mail(
        from_email=sender,
        to_emails=recipients,
        subject="🗞️ Your Daily Tech Digest",
        html_content=content
    )

    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print("Email sent:", response.status_code)
    except Exception as e:
        print("Error sending email:", str(e))

if __name__ == "__main__":
    send_email()
