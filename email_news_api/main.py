import requests
from emailer import send_email

api_key = "5a122da0c5cb444b9a2e0f127973fd62"
topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2023-02-06&sortBy=publishedAt&apiKey=" \
      f"{api_key}&language=en"

# request
request = requests.get(url)
# data as dict
content = request.json()
# loop through
n = 0
email_data = ""
for article in content['articles'][0:20]:
    # n += 1
    # print(f"{n}. {article['title']}")
    # print(f"{article['description']}")
    title = article['title']
    description = article['description']
    email_data = email_data \
                 + article['title'] \
                 + article['description'] \
                 + "\n" \
                 + article['url'] \
                 + 2 * "\n"

email_data = email_data.encode('utf-8')



send_email(message=email_data)
