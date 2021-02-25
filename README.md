# Stock Alerts
Program that allows you to track the current & previous close price of a given company's shares every 30 minutes and send that information to a Discord channel.

# Why?
What is the point of this program when you can literally open up your favorite stock trading app and view detailed information about a given share? To limit the number of times you are picking up your phone or viewing websites. Looking at stocks can get addicting fairly quickly when you have money invested within the market. Looking at stock prices Monday-Friday can suddenly increase your phone pick-ups, unlocks and usage subtantially. This program aims to limit that to twice per hour giving you the current price and percent change from it's pervious close every 30 minutes.

# Requirements
Install package
```sh
pip install discord-webhook
```

A [Finhubb.io](https://finnhub.io/) account for a free API key

A Discord account, channel and [Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

# Usage
To start, the program will ask you which companies you would like to track for the day. Enter each company using their stock symbol in a comma separated manner. 
```sh
TSLA,AAPL,AMZN,MSFT
```
The Program will continue to run until it is cancelled by the user or the time reaches 21:00 (UTC)
