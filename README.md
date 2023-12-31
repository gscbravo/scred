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

for i, entry in enumerate(scred.get_posts('todayilearned', 2)):
    print(f"INDEX: {i}")
    print(f"author: {entry['author']}")
    print(f"comments: {entry['comments']}")
    print(f"id: {entry['id']}")
    print(f"link: {entry['link']}")
    print(f"timestamp: {entry['timestamp']}")
    print(f"title: {entry['title']}")
    print(f"votes: {entry['votes']}")
    print('---')
```

## get_metadata(subreddit, session = None)

Returns dictionary of metadata about subreddit.

### Arguments

| argument       | purpose                                              |
| -------------- | ---------------------------------------------------- |
| subreddit      | subreddit name, without 'r/'                         |
| session = None | 'reddit_session' cookie, used for private subreddits |

### Returns

Dictionary containing:

| key         | value                       |
| ----------- | --------------------------- |
| description | subreddit description       |
| members     | number of subreddit members |
| online      | number of members online    |
| title       | full title of the subreddit |

## get_posts(subreddit, pages = 1, session = None)

Returns a list of posts on subreddit. Gets around 25 posts per page.

### Arguments

| argument       | purpose                                              |
| -------------- | ---------------------------------------------------- |
| subreddit      | subreddit name, without 'r/'                         |
| pages = 1      | number of pages to retrieve, default is 1            |
| session = None | 'reddit_session' cookie, used for private subreddits |

### Returns

List of dictionaries each containing:

| key       | value                                                        |
| --------- | ------------------------------------------------------------ |
| author    | poster username, without 'u/'                                |
| comments  | link to the post comments                                    |
| id        | post short id                                                |
| link      | link given by the post, if none is given, same as 'comments' |
| thumbnail | thumbnail preview for picture                                |
| timestamp | ISO 8601 timestamp in UTC. Ex: YYYY-MM-DDThh:mm:ss+00:00     |
| title     | title of the post                                            |
| votes     | number of votes the post has                                 |

## TODO

- [ ] Get the various subreddit icons and banners
- [ ] Get the subreddit rules
- [ ] Get comments given a post
- [ ] Get posts given a username
- [ ] Take a look at the subreddit.json file for each subreddit for more data
