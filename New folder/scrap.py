import requests
from bs4 import BeautifulSoup

# URL of the single page
url = "https://www.dhakatribune.com/bangladesh"

# Send GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract text data (e.g., news titles)
text_data = []

articles = soup.find_all("article")  # Adjust selector based on the page structure

for article in articles:
    title_tag = article.find("h3", class_="post-title")  # Example; adjust as necessary
    if title_tag:
        text_data.append(title_tag.get_text(strip=True))

# Join all text data into a single corpus
corpus = " ".join(text_data)

print("Scraped Data:")
print(corpus[:500])  # Print the first 500 characters of the corpus