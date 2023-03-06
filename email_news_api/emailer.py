import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("SENDER_EMAIL")
    password = os.getenv("STREAMLIT_EMAIL_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # server.starttls()
        server.login(username, password)
        server.sendmail(username, receiver_email, message)
