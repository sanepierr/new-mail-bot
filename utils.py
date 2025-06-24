import feedparser

FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "CNET": "https://www.cnet.com/rss/news/",
    "Engadget": "https://www.engadget.com/rss.xml",
    "Ars Technica": "https://feeds.arstechnica.com/arstechnica/index"
}

def get_headlines(limit=3):
    headlines = []
    for name, url in FEEDS.items():
        feed = feedparser.parse(url)
        entries = feed.entries[:limit]
        for entry in entries:
            headlines.append({
                "source": name,
                "title": entry.title,
                "link": entry.link
            })
    return headlines

def format_email(headlines):
    body = "<b>Tech News Digest</b><br><br>"
    for item in headlines:
        body += f"<b>{item['source']}</b>: <a href='{item['link']}'>{item['title']}</a><br><br>"
    body += "<br>--<br><i>Sent by Tech News Bot</i>"
    return body
