import asyncio
import telegram
from telegram import Bot
import requests
from bs4 import BeautifulSoup
import nest_asyncio
import pyshorteners
import datetime


async def send_cybersecurity_news():
    # Get the current day
    today = datetime.date.today()

    # Perform a Google News search for "cybersecurity" and only return results from the current day
    url = f"https://news.google.com/search?q=cybersecurity&hl=en-US&gl=US&ceid=US%3Aen&tbs=cdr:1,cd_min:{today},cd_max:{today}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all news articles on the page
    articles = soup.find_all("article")

    # Connect to the Telegram bot using the API token obtained from BotFather
    bot = Bot(token='6058266858:AAHCAY8h9SVr6u6KNG8SuNqrs_w1L7rDeqc')

    # Use a URL shortener to shorten the links
    shortener = pyshorteners.Shortener()

    # Send each news article title and shortened link to the Telegram channel
    for article in articles:
        title = article.find("a", class_="DY5T1d").text
        link = "https://news.google.com" + article.find("a")["href"][1:]
        shortened_link = shortener.tinyurl.short(link)
        message = f"{title}\n\n\n\nRead more: {shortened_link}\n"
        try:
            await bot.send_message(chat_id='@Cyber0xSleuth', text=message)
        except telegram.error.TimedOut:
            print("Timed out sending message")


async def main():
    # Send the news articles to the Telegram channel
    await send_cybersecurity_news()


if __name__ == "__main__":
    # Import nest_asyncio and apply it
    nest_asyncio.apply()

    # Run the event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
