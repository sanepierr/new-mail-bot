# news-mail-bot
Automatically fetches the latest technology news from top sites (via RSS feeds) and sends daily summary emails to a list of recipients using SendGrid.


# Tech News Email Bot

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Platform](https://img.shields.io/badge/hosted%20on-render-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

This Python-based bot automatically pulls the latest technology news from top sources and emails it to a list of recipients twice a day — at **7:00 AM** and **11:00 PM (EAT)**. Perfect for staying up-to-date without checking multiple sites.


## Features

- Aggregates headlines via **RSS feeds** from:
  - [TechCrunch](https://techcrunch.com/feed/)
  - [The Verge](https://www.theverge.com/rss/index.xml)
  - [CNET](https://www.cnet.com/rss/news/)
  - [Engadget](https://www.engadget.com/rss.xml)
  - [Ars Technica](https://feeds.arstechnica.com/arstechnica/index)
-  Sends well-formatted emails using **SendGrid**
-  Supports multiple recipients
-  Automatically runs at scheduled times
-  Deployable on **Render (free tier)**

---

##  How It Works

1. Fetch headlines from RSS feeds
2. Format a clean email digest
3. Send via SendGrid's transactional email API
4. Run automatically twice daily using a scheduler

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/sanepierr/tech-news-email-bot.git
cd tech-news-email-bot


pip install -r requirements.txt
SENDGRID_API_KEY=your_sendgrid_api_key
SENDER_EMAIL=your_verified_sender@example.com
RECIPIENT_EMAILS=email1@example.com,email2@example.com
TIMEZONE=Africa/Kampala
