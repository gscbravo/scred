# scred

## About

Simple web scraper for [Reddit](https://old.reddit.com), inspired by
[recent events](https://en.wikipedia.org/wiki/2023_Reddit_API_controversy).

Use responsibly, etc.

[Relevant court case](https://en.wikipedia.org/wiki/HiQ_Labs_v._LinkedIn).

## Usage

Install requirements:

```
pip3 install requests beautifulsoup4 lxml
```

Import the module:

```python
import scred

for entry in scred.get_subreddit('todayilearned'):
    print(f"author: {entry['author']}")
    print(f"comments: {entry['comments']}")
    print(f"link: {entry['link']}")
    print(f"timestamp: {entry['timestamp']}")
    print(f"title: {entry['title']}")
    print(f"votes: {entry['votes']}")
    print('---')
```

## get_subreddit(subreddit, session = None)

Returns a list of first page posts on subreddit.

### Arguments

| argument       | purpose                                              |
| -------------- | ---------------------------------------------------- |
| subreddit      | subreddit name, without 'r/'                         |
| session = None | 'reddit_session' cookie, used for private subreddits |

### Returns

| key       | value                                                        |
| --------- | ------------------------------------------------------------ |
| author    | poster username, without 'u/'                                |
| comments  | link to the post comments                                    |
| link      | link given by the post, if none is given, same as 'comments' |
| timestamp | ISO 8601 timestamp in UTC. Ex: YYYY-MM-DDThh:mm:ss+00:00     |
| title     | title of the post                                            |
| votes     | number of votes the post has                                 |

## TODO

- [ ] Show more than just the first page
- [ ] Get comments given a post
- [ ] Get posts given a username
- [ ] Maybe be honest and use some custom User-Agent instead of Chrome's
	- Just maybe
	- `Mozilla/5.0 (compatible; scred/1.0; +https://github.com/gscbravo/scred)`
