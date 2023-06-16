# scred

## About

Simple web scraper for [Reddit](https://old.reddit.com), inspired by recent
events. You input the name of a subreddit and then it will display the
posts onto the terminal.

If you make changes, make sure to keep the
[User-Agent](https://en.wikipedia.org/wiki/User_agent) as something, Reddit
seems to be able to detect and rate limit User-Agents if they're nothing or
that of a common web scraping library, like that of
[Requests](https://requests.readthedocs.io/en/latest/)'s. Output is displayed
in Markdown.

I'm considering turning this into a module instead of a terminal output
program.

Use responsibly, etc.

[Relevant court case](https://en.wikipedia.org/wiki/HiQ_Labs_v._LinkedIn).

## Usage

```
pip3 install flask beautifulsoup4 lxml
python3 scred.py
```

## TODO

- [ ] Show NSFW subreddits
- [ ] Allow providing cookies to show private subreddits
	- This might be a violation of the
	[CFAA](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act), as I
	believe there might be a thing against creating accounts specifically
	to scrape, need to do more research on this
- [ ] Display comments
- [ ] Might turn into a module
