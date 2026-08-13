# Books Scraper & Telegram Bot

Automated Python application that scrapes book data from Books to Scrape, filters top-rated items, exports data to CSV, and sends reports via Telegram Bot API.

## Features

- Automated Web Scraping: Scrapes all 50 pages of the catalogue using BeautifulSoup.
- Smart Filtering: Extracts only books with a 5-star rating.
- Data Export: Formats and saves data into a clean CSV file with UTF-8 encoding.
- Telegram Bot Integration: Automatically delivers text alerts and CSV documents directly to a Telegram Chat.
- Infinite Loop Execution: Designed to run continuously on a set timer interval.

## Tech Stack

- Language: Python 3
- Libraries: requests, beautifulsoup4, csv, time
- API: Telegram Bot API
