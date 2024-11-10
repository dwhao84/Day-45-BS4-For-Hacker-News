# Hacker News 爬蟲程式

這是一個簡單的 Python 爬蟲程式，用於抓取 Hacker News 網站的文章資訊。程式會擷取文章標題、連結和投票數，並找出最多人投票的文章。

## 功能說明

程式會：
1. 連接到 Hacker News 網站
2. 擷取所有文章的標題和連結
3. 收集每篇文章的投票數
4. 找出並顯示最多人投票的文章資訊

## 使用的套件

```python
from bs4 import BeautifulSoup
import requests
import re
```

## 安裝需求

在使用此程式前，請先安裝必要的套件：

```bash
pip install beautifulsoup4
pip install requests
```

## 程式碼說明

```python
# 設定 Hacker News 網址
hacker_news_url = "https://news.ycombinator.com/"

# 發送 GET 請求獲取網頁內容
response = requests.get(hacker_news_url)
yc_webpage = response.text

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(yc_webpage, "html.parser")

# 找出所有文章標題
articles = soup.find_all(name="span", class_="titleline")

# 儲存文章標題和連結
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name='a').get("href")
    article_links.append(link)

# 擷取所有文章的投票數
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# 找出最多投票的文章
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
```

## 輸出結果

程式會印出：
1. 所有文章的標題列表
2. 所有文章的連結列表
3. 所有文章的投票數列表
4. 最多人投票文章的標題
5. 最多人投票文章的連結
6. 最多人投票文章的投票數

## 使用範例

```python
# 執行程式後的輸出範例：
print(article_texts)        # 印出所有文章標題
print(article_links)        # 印出所有文章連結
print(article_upvotes)      # 印出所有文章投票數
print(article_texts[largest_index])      # 印出最多投票文章的標題
print(article_links[largest_index])      # 印出最多投票文章的連結
print(article_upvotes[largest_index])    # 印出最多投票文章的投票數
```

## 注意事項

1. 請確保網路連線正常
2. 需要遵守 Hacker News 的使用條款
3. 網站結構可能會改變，屆時需要更新程式碼
4. 建議不要過於頻繁地執行程式，以避免對伺服器造成負擔

## 可能的改進方向

1. 加入錯誤處理機制
2. 新增資料儲存功能
3. 實作定時抓取功能
4. 加入更多資料分析功能
5. 優化程式碼結構

## License

MIT License 