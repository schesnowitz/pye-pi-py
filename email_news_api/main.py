import requests
from emailer import send_email
api_key = "5a122da0c5cb444b9a2e0f127973fd62"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-02-06&sortBy=publishedAt&apiKey=" \
      "5a122da0c5cb444b9a2e0f127973fd62"

# request
request = requests.get(url)
# data as dict
content = request.json()
# loop through
n = 0
email_data = ""
for article in content['articles']:
    # n += 1
    # print(f"{n}. {article['title']}")
    # print(f"{article['description']}")
    title = article['title']
    description = article['description']
    email_data = email_data + title + "\n" + description + 2* "\n"

email_data = email_data.encode('utf-8')

send_email(message=email_data)

