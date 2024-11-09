from bs4 import BeautifulSoup
import requests
import re

hacker_news_url = "https://news.ycombinator.com/"

response = requests.get(hacker_news_url) # 訪問hacker news
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser") # 用soup讀取response後的資料。
# print(soup) # 印出soup

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name='a').get("href")
    article_links.append(link)

print(article_texts)
print(article_links)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])