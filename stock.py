
def send_discord_message(message):
    from discord_webhook import DiscordWebhook
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/777733965683359745/1fMsIIX21V9EbNL5Z0yOiQG8NYnVPcju9hU8zi1xAljei_XSx8xQyNOPRxIh7-_htro8", content=message)
    reponse = webhook.execute()

def user_input():
    n = str(input("Enter the stock symbols you would like to track for the day separating them with commas: ")).replace(' ', '')
    stocks = n.split(",")
    return stocks
    

def stock_info():
    import requests
    string = ""
    for stock in stocks:
        r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={stock}&token=c0h17e748v6ttm1suvl0')
        string = string + f"{stock}\nPrevious close: {r.json()['pc']}\nCurrent price: {r.json()['c']}\nPrecent change: {str(round((r.json()['c'] - r.json()['pc']) / r.json()['pc'] * 100, 2))}\n\n"
    return string


def run_continuously(time_in_seconds):
    import time
    from datetime import datetime

    now = datetime.utcnow()
    market_open = now.replace(hour=14, minute=30, second=0, microsecond=0)
    market_close = now.replace(hour=21, minute=0, second=0, microsecond=0)
    starttime = time.time()
    while True:
        if now >= market_open and now <= market_close:
            send_discord_message(stock_info())
            time.sleep(time_in_seconds - ((time.time() - starttime) % time_in_seconds))
        else:
            exit()

stocks = user_input()
run_continuously(1800)






    
