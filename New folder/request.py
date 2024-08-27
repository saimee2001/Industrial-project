import newspaper
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import re
from newspaper import Config




data = []

url = "https://www.dhakatribune.com/bangladesh"  # Replace with the target URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

base_url = url  # Base URL for joining relative links
links = []

for a_tag in soup.find_all('a', href=True):
    link = urljoin(base_url, a_tag['href'])  # Join relative URLs with the base URL
    links.append(link)



filtered_links = [link for link in links if link.startswith("https://www.dhakatribune.com/bangladesh/")]



for i in filtered_links:
    try:
        article = newspaper.Article(i)
        article.download()
        article.parse()


    
        match = re.search(r'/bangladesh/([^/]+)/\d+', i)

        if match:
            extracted_text = match.group(1)
        else:
            continue

        others = ['politics', 'crime','dhaka','education']
        
        for j in others:
            if extracted_text == j:
                continue
        
        
        # article.nlp(); summarization ta kaj korse na. i think amr path e problem hoise. apnar env e try kore dekhen hoi kina.

        item = {
            'link':i,
            'title': article.title,
            'authors': article.authors,
            'published_date': article.publish_date,
            'category': extracted_text,
            'text': article.text,
            #'summary':article.summary
        }
        
        data.append(item)
        
    except newspaper.ArticleException as e:
        print(f"Failed to process article at {i}: {e}")
        continue


df = pd.DataFrame(data)

df.to_csv("books.csv")


print("File saved successfully.")