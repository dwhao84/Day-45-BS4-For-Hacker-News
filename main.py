from bs4 import BeautifulSoup
import requests
import re

hacker_news_url = "https://news.ycombinator.com/"

response = requests.get(hacker_news_url) # 訪問hacker news
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser") # 用soup讀取response後的資料。
# print(soup) # 印出soup

# 用soup找到name為span，class為titleline。
article_tag = soup.find(name='span', class_="titleline")
print(article_tag.get_text()) # 印出title line。

# 印出article link，找到a的tag，用get找href的資料。
article_link = article_tag.find(name="a").get("href")
print(article_link)

# 印出article upvote
article_upvote = soup.find(name='span', class_='score')
print(article_upvote.get_text())