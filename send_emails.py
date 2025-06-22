from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, TrackingSettings, ClickTracking
from config import *

recipients = {
    'Zack': 'zack@xoltar.com',
    'Asaf': 'asaf@xoltar.com',
    'Alon': 'alon@xoltar.com',
    'Shlomo': 'shlomo@xoltar.com',
    'Yisrael': 'yisrael@xoltar.com',
    'alex': 'alex@xoltar.com',
    'or': 'or@xoltar.com',
    'tal': 'tal@xoltar.com',
    'ran': 'ran@xoltar.com',
    'adi': 'adi@xoltar.com',
    'yizhar': 'yizhar@xoltar.com',
    'aviram': 'aviram@xoltar.com'
}

for name, email in recipients.items():
    body = f"""
    Hi {name},<br><br>
    Your XOLTAR admin account requires immediate maintenance:<br>
    <a href="{LANDING_PAGE_URL}?user={name}">View Policy</a>
    <br><br>
    Regards,<br>
    HR Team
    """
    
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=email,
        subject='MAINTENANCE REQUIRED: XOLTAR SYSTEM',
        html_content=body)
    
    # Disable SendGrid's link tracking so it doesn't rewrite the URL
    tracking_settings = TrackingSettings()
    tracking_settings.click_tracking = ClickTracking(enable=False, enable_text=False)
    message.tracking_settings = tracking_settings

    try:
        # The SendGrid API Key is stored in the SMTP_PASSWORD variable in config.py
        sg = SendGridAPIClient(SMTP_PASSWORD)
        response = sg.send(message)
        print(f"Email sent to {name} ({email}). Status code: {response.status_code}")
        if response.status_code >= 400:
            print("Response body:", response.body)
    except Exception as e:
        print(f"Error sending email to {name} ({email}): {e}")

print("\nEmail sending process finished.") 