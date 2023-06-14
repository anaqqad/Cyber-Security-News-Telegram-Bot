# Cyber Security News Telegram Bot

A Python script that scrapes the web for cyber security news and sends it to a Telegram channel.

<div style="text-align: center;">
  <img src="telegram_channel.jpg" alt="A cyber security news channel in Telegram." width="300">
</div>

## Overview

This script allows you to scrape the web for the latest cyber security news and send it to a specified Telegram channel using a Telegram bot. The script performs a Google News search for "cybersecurity" and retrieves news articles from the current day. It then shortens the article links and sends each article's title and shortened link to the Telegram channel.

## Prerequisites

To run the script, you'll need the following:

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- `beautifulsoup4` library (`pip install beautifulsoup4`)
- `pyshorteners` library (`pip install pyshorteners`)
- `python-telegram-bot` library (`pip install python-telegram-bot`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cyber-security-news-bot.git

2. Install the required dependencies:

   pip install -r requirements.txt

3. Obtain a Telegram Bot API token:

  - Go to BotFather on Telegram.
  - Start a chat with BotFather by clicking on the "Start" button.
  - Type /newbot and follow the instructions to create a new bot.
  - Choose a name for your bot (e.g., "CyberSleuthBot") and a unique username (e.g., "@cyber_sleuth_bot").
  - After successfully creating the bot, BotFather will provide you with an API token. Copy this token as you'll need it later.

4. Configure the Telegram Bot API token:

  - Open the CyberSleuthBot.py file in a text editor.
  - Find the line bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN').
  - Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the API token obtained from BotFather. The line should look like: bot = Bot(token='your_token_here')

5. Customize the script (optional):

  - You can customize the behavior of the script by modifying the following:
  - Telegram Channel: Change the chat_id parameter in the line await bot.send_message(chat_id='@Cyber0xSleuth', text=message) in the telegram_bot.py script. Replace @Cyber0xSleuth with your desired Telegram channel username or ID.
  - Search Query: If you want to change the search query from "cybersecurity" to something else, modify the URL in the send_cybersecurity_news() function in the news_scraper.py script.

6. Run the script:

python CyberSleuthBot.py

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This mini-project is licensed under the MIT License. 

You can copy the revised content above and replace the existing content in your `README.md` file. Make sure to review and update the instructions according to your specific project details.
