# See: "requests library Tutorial" module (in this project)

import requests
from send_email import send_email
from send_email_2 import send_email_2

# Not very useful to just get the contents of web page (which is meant to be read by humans)
# url = "https://finance.yahoo.com"
# r = requests.get(url)
# content = r.text
# print(content)

# More useful to get the contents of an API (which is designed to be read by computers)

api_key = "596005ba759644559a58f1f80a18c0c4"

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-04-10&sortBy=publishedAt&apiKey=" + api_key

# Make a request
r = requests.get(url)
# content = r.text
# print(content)
# print(type(content))  # <class str>  Not very usable in this format

# Get a dictionary with data
content = r.json()  # Make data more accessible:
# print(content)
# print(type(content))  # <class dict>
# print(content["articles"])

# Access the article titles and descriptions within the dictionary
message = ""
for article in content["articles"]:
    # print(article["title"])
    # print(article["description"])

    title = article["title"]
    description = article["description"]

    # Handle situations in which title and/or description are 'None'
    if title:
        message += title + '\n'
    else:
        message += "[No Title]" + '\n'

    if description:
        message += description + (2 * '\n')
    else:
        message += "[No Description]" + (2 * '\n')

# Method 1:
# ---------
# message = """\
# Subject: Latest Tesla News
#
# """ + message                      # Insert Subject at start of message
# message = message.encode("utf-8")  # Convert to UTF-8 encoding
# send_email(message)

# Method 2:
# ---------
send_email_2(subject="Latest Tesla News", message=message)
