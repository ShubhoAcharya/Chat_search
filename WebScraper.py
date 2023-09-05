from bs4 import BeautifulSoup
import requests
import re


# Define the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/Narendra_Modi'

# Send an HTTP request to the URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Create a Beautiful Soup object with the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Print the title of the webpage
title = soup.title.text
print("Title:", title)

# Define the pattern you want to subtract or remove
pattern = "\[\d*\w]"

data=[]

# Find and print all the paragraphs on the webpage
print("Paragraphs:")
for paragraph in soup.find_all('p'):
    if not paragraph.find_parent('table'):
        data.append(re.sub(pattern, "", paragraph.text))

for i in data:
    print(i)