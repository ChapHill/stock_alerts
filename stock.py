
def send_discord_message(message):
    from discord_webhook import DiscordWebhook
    webhook = DiscordWebhook(url="YOUR_WEBHOOK_URL_HERE", content=message)
    reponse = webhook.execute()

def user_input():
    n = str(input("Enter the stock symbols you would like to track for the day separating them with commas: ")).replace(' ', '')
    stocks = n.split(",")
    return stocks
    

def stock_info():
    import requests
    string = ""
    for stock in stocks:
        r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={stock}&token=YOUR_FINNHUBB_KEY_HERE')
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






    
