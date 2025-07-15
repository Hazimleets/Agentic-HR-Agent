# chatbot3/tools/gmail_api.py
def send_email(to, subject, content):
    print(f"Sent email to {to}. Subject: {subject}\n{content}")
    return {"status": "sent", "service": "Gmail"}