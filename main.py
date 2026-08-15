import csv
import time
import requests
from bs4 import BeautifulSoup

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

while True:
    books=[]

    print("\n--- STARTING NEW SCRAPING CYCLE ---")

    for page in range(1, 51):
        url=f"http://books.toscrape.com/catalogue/page-{page}.html"
        res=requests.get(url)
        res.encoding="utf-8"
        soup=BeautifulSoup(res.text, "html.parser")

        products=soup.find_all("article", class_="product_pod")

        for p in products:
            title=p.find("h3").find("a")["title"]
            rating=p.find("p", class_="star-rating Five")

            if rating:
                books.append({"title": title, "rating": "5 Stars"})

    print(f"Scraping completed! Found a total of {len(books)} books.")

    filename="5_star_books.csv"

    with open(filename, mode="w", newline="", encoding="utf-8-sig") as f:
        writer=csv.DictWriter(f, fieldnames=["title", "rating"])
        writer.writeheader()
        writer.writerows(books)

    print(f"Data successfully saved to file: {filename}")

    msg=(
        f"🚀 **Scraper finished execution!**\n"
        f"Found a total of **{len(books)}** books with a 5-star rating.\n"
        f"The complete list is attached in the CSV file below! 👇"
    )

    text_url=f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(
        text_url,
        data={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"},
    )

    doc_url=f"https://api.telegram.org/bot{TOKEN}/sendDocument"

    with open(filename, "rb") as doc:
        res=requests.post(
            doc_url,
            data={"chat_id": CHAT_ID},
            files={"document": doc},
        )

    if res.status_code==200:
        print("CSV file successfully sent to Telegram! 🎉")
    else:
        print("Error sending document:", res.json())

    pause=60
    print(
        f"Cycle finished! Script sleeping for {pause} seconds before restarting...\n"
    )

    time.sleep(pause)u
