import smtplib, ssl
import os
import imghdr
from email.message import EmailMessage
def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New webcam activity"
    email_message.set_content("See the attached image")


    with open(image_path, 'rb') as file:
        image_content = file.read()
    email_message.add_attachment(image_content,
                                 maintype="image",
                                 subtype=imghdr.what(None, image_content))
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("SENDER_EMAIL")
    password = os.getenv("STREAMLIT_EMAIL_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")
    context = ssl.create_default_context()


    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver_email, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/92.png")