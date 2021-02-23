
def send_discord_message(message):
    from discord_webhook import DiscordWebhook
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/777733965683359745/1fMsIIX21V9EbNL5Z0yOiQG8NYnVPcju9hU8zi1xAljei_XSx8xQyNOPRxIh7-_htro8", content=message)
    reponse = webhook.execute()

def user_input():
    n = str(input("Enter the number of companies you would like to track for the day separated by commas: ")).replace(' ', '')
    stocks = n.split(",")
    return stocks
    

def stock_info():
    import requests
    stocks = user_input()
    for stock in stocks:
        print(stock)
        r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={stock}&token=c0h17e748v6ttm1suvl0')
        print(r.json())
        print()


    """ import time
    starttime = time.time()
    while True:
        print("tick")
        time.sleep(1800.0 - ((time.time() - starttime) % 1800.0)) """


stock_info()



    
