import requests
from bs4 import BeautifulSoup

# legit User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; scred/1.0; +https://github.com/gscbravo/scred)'
}

def get_subreddit(subreddit, pages = 1, session = None):
    '''
    Returns a list of first page posts on subreddit.

    Args:
        subreddit:
            subreddit name, without 'r/'
        pages = 1:
            number of pages to retrieve, default is 1
        session = None:
            'reddit_session' cookie, used for private subreddits

    Returns:
        List of dictionaries each containing:
            author:
                poster username, without 'u/'
            comments:
                link to the post comments
            id:
                post short id
            link:
                link given by the post, if none is given, same as 'comments'
            timestamp:
                ISO 8601 timestamp in UTC
                Ex: YYYY-MM-DDThh:mm:ss+00:00
            title:
                title of the post
            votes:
                number of votes the post has
    '''

    # cookies to allow viewing gated and NSFW subreddit
    cookies = {
        '_options': '%7B%22pref_gated_sr_optin%22%3A%20true%7D',
        'over18': '1',
        'reddit_session': session if session is not None else ''
    }

    url = f"https://old.reddit.com/r/{subreddit}/"
    posts = []

    # go through the pages
    for i in range(pages):
        response = requests.get(url, headers=headers, cookies=cookies)
        soup = BeautifulSoup(response.content, 'lxml')

        # get the posts, exclude ads
        for entry in soup.select('div.link:not(.promoted)'):
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

            # get votes
            entry_votes = entry.select_one('div.score').text

            # get timestamp
            entry_timestamp = entry.select_one('time.live-timestamp')['datetime']

            # get id
            entry_id = entry_comments.split('/')[6]

            # add the info
            posts.append({
                'author': entry_author,
                'comments': entry_comments,
                'id': entry_id,
                'link': entry_link,
                'timestamp': entry_timestamp,
                'title': entry_title,
                'votes': entry_votes
            })

        # get the next button and set url to it, escape if it doesn't exist
        next_page = soup.select_one('span.next-button a')
        if next_page is None:
            return posts
        
        url = next_page['href']
    
    return posts
