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

print("News Finder:")

topic = ""
while not topic:
    topic = input("What are you searching for? ").strip().lower()

topic = '"' + topic + '"'  # surround phrase with quotes (eg: "star wars")
print("Processing...")

# Search all elements of dictionary for "Tesla" (&everything?q=tesla)
# Select articles published 4/10/24 and later (&from=2024-04-10)
# Select English only (&language=en)
# Select a max of 50 articles (&pageSize=50)
# Sort by publication date (&sortBy=publishedAt)
url = f"https://newsapi.org/v2/everything?q={topic}" \
      "&from=2024-04-10" \
      "&language=en" \
      "&pageSize=50" \
      "&sortBy=publishedAt" \
      f"&apiKey={api_key}"

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
for article in content["articles"][:20]:  # Only process 1st 20 articles
    title = article["title"].strip()
    description = article["description"].strip()
    url = article["url"]

    # Handle situations in which title and/or description are 'None'
    if title == "[Removed]":  # Drop articles that are flagged as "[Removed]"
        continue
    elif title:
        message += title + '\n'
    else:
        message += "[No Title]" + '\n'

    if description:
        message += description + '\n'
    else:
        message += "[No Description]" + '\n'

    if url:
        message += url + (2 * '\n')
    else:
        message += "[No Link]" + (2 * '\n')

# Method 1:
# ---------
# message = f"""\
# Subject: Latest {topic.strip('"').title()} News
#
# """ + message                      # Insert Subject at start of message
# message = message.encode("utf-8")  # Convert to UTF-8 encoding
# send_email(message)

# Method 2:
# ---------
send_email_2(subject=f"Latest {topic.title()} News", message=message)
print("Your email was sent successfully.")
