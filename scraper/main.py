import requests
import selectorlib
import os
import smtplib, ssl
import os
import time
import sqlite3


connection = sqlite3.connect("database.db")



URL = os.getenv("SRAPE_SITE")
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape info from url"""
    response = requests.get(url, HEADERS)
    page_data = response.text
    return page_data


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

    print("Email was sent")


def extract(page_data):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(page_data)["tours"]
    # print(value)
    return value


def data_store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()
def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute(
    "SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()
    print(rows)
    return rows


if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)


        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                data_store(extracted)
                send_email(message=f"new data found {extracted}")
        time.sleep(3)
