import requests
from bs4 import BeautifulSoup

# User-Agent set to Chrome 114 on Windows 10 to avoid rate limit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
url = f"https://old.reddit.com/r/{input('# r/').strip()}/"
print("")
soup = BeautifulSoup(requests.get(url, headers=headers).content, 'lxml')

for entry in soup.select('div.link:not(.promoted) div.entry'):
    # get entry author, setting to [deleted] if not present
    author_link = entry.select_one('a.author')
    if author_link is not None:
        entry_author = author_link.text
    else:
        entry_author = '[deleted]'

    # get entry title
    entry_title = entry.select_one('a.title').text

    # get entry link, determining whether relative link or not
    entry_href = entry.select_one('a.title')['href']
    if not entry_href.startswith('/'):
        entry_link = entry_href
    else:
        entry_link = f"https://old.reddit.com{entry_href}"

    # get commnts
    entry_comments = entry.select_one('a.comments')['href']

    # print entry, add comments if the link was not the comments
    print(f"[{entry_author}: {entry_title}]({entry_link})\n")
    if entry_link != entry_comments:
        print(f"[Comments]({entry_comments})\n")
    print("***\n")
