# scred

## About

Simple web scraper for [Reddit](https://old.reddit.com), inspired by recent
events. If you make changes, make sure to keep the
[User-Agent](https://en.wikipedia.org/wiki/User_agent) as something, Reddit
seems to be able to detect and rate limit User-Agents if they're nothing or
that of a common web scraping library, like that of
[Request](https://requests.readthedocs.io/en/latest/)'s. Output is displayed
in Markdown.

## Usage

```
pip3 install flask beautifulsoup4 lxml
python3 scred.py
```

## TODO

- [ ] Display comments
