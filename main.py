# See: "requests library Tutorial" module (in this project)
import requests
import smtplib as smtp
from send_email import send_email

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
message = """\
Subject: Latest Tesla News

"""
for article in content["articles"]:
    # print(article["title"])
    # print(article["description"])

    title = article["title"]
    description = article["description"]
    message += title + '\n'
    message += description + '\n'
    message += '\n'

# Email titles and descriptions to myself
# send_email(message)
