
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
    stocks = user_input()
    string = ""
    for stock in stocks:
        r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={stock}&token=c0h17e748v6ttm1suvl0')
        string = string + f"{stock}\nPrevious close: {r.json()['pc']}\nCurrent price: {r.json()['c']}\nPrecent change: {str(round((r.json()['c'] - r.json()['pc']) / r.json()['pc'] * 100, 2))}\n\n"
    return string


    """ import time
    starttime = time.time()
    while True:
        print("tick")
        time.sleep(1800.0 - ((time.time() - starttime) % 1800.0)) """


send_discord_message(stock_info())



    
