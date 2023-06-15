import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
url = f"https://old.reddit.com/r/{input('# r/').strip()}/"
print("")
soup = BeautifulSoup(requests.get(url, headers=headers).content, 'lxml')

for entry in soup.select('div.link:not(.promoted) div.entry'):
    entry_author = entry.select_one('a.author').text if entry.select_one('a.author') is not None else '[deleted]'
    entry_title = entry.select_one('a.title').text
    entry_link = entry.select_one('a.title')['href'] if not entry.select_one('a.title')['href'].startswith('/') else f"https://old.reddit.com{entry.select_one('a.title')['href']}"
    entry_comments = entry.select_one('a.comments')['href']
    print(f"[{entry_author}: {entry_title}]({entry_link})")
    if entry_link != entry_comments:
        print(f"[Comments]({entry_comments})")
    print("***")
