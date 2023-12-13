import time
import logging
from binance.lib.utils import config_logging
from binance.spot import Spot as Client
from binance.websocket.spot.websocket_client import SpotWebsocketClient
from connectiontoAPI import *
from DataSets import *
import pandas as pd


config_logging(logging, logging.DEBUG)

def message_handler(message):
    print("работаєм 1 ", message)

api_key = test_net_key
client = Client(api_key, test_net_sekret, base_url="https://testnet.binance.vision")

a = [{'asset': 'BNB', 'free': '1000.00000000', 'locked': '0.00000000'}, {'asset': 'BTC', 'free': '0.80000000', 'locked': '0.00000000'}, {'asset': 'BUSD', 'free': '10000.00000000', 'locked': '0.00000000'}, {'asset': 'ETH', 'free': '100.00000000', 'locked': '0.00000000'}, {'asset': 'LTC', 'free': '500.00000000', 'locked': '0.00000000'}, {'asset': 'TRX', 'free': '500000.00000000', 'locked': '0.00000000'}, {'asset': 'USDT', 'free': '14140.46414000', 'locked': '0.00000000'}, {'asset': 'XRP', 'free': '50000.00000000', 'locked': '0.00000000'}]


# записать в if __name__ == "__main__":
account = client.account()

def wallet_spot_data(balances):
    for i in range(len(balances)):
        coin_name = balances[i].get('asset')
        DataSpotRealTime.set('asset' + coin_name, balances[i].get('asset'))
        DataSpotRealTime.set('free' + coin_name, balances[i].get('free'))
        DataSpotRealTime.set('locked' + coin_name, balances[i].get('locked'))

print(account)
wallet_spot_data(account.get('balances'))
print(DataSpotRealTime.check())
#qwe = ["BTCUSDT","BNBBTC"]

#asd = client.exchange_info(symbols=qwe)
#print(asd)
response = client.new_listen_key()

#print("работаєм", response)
logging.info("Receving listen key : {}".format(response["listenKey"]))

ws_client = SpotWebsocketClient(stream_url="wss://testnet.binance.vision")

ws_client.start()

#print(response["listenKey"])
#print(pd.DataFrame(client.account().get('balances')))

def new_order(symbol, type_side, quantity, price):
    params = {
            'symbol': symbol,
            'side': type_side,
            'type': 'LIMIT',
            'timeInForce': 'GTC',
            'quantity': quantity, #проблема
            'price': price
    }
    client.new_order(**params)

ws_client.user_data(
    listen_key=response["listenKey"],
    id=1,
    url_path = "/api/v3/account",
    callback=message_handler,
)

time.sleep(10)
print("nachalo")

new_order('BTCUSDT', 'BUY', 0.1, 18000)
print(pd.DataFrame(client.account().get('balances')))

new_order('BTCUSDT', 'SELL', 0.1, 21000)
print(pd.DataFrame(client.account().get('balances')))

#response = client.cancel_open_orders('BTCUSDT')
df = pd.DataFrame(
    client.get_orders(symbol = 'BTCUSDT'),
    columns=['orderId', 'type', 'side', 'price', 'status']
)

print(df.tail(15))
print(pd.DataFrame(client.account().get('balances')))

time.sleep(5)

logging.debug("closing ws connection")
ws_client.stop()

"""from binance.spot import Spot
from connectiontoAPI import *
import pandas as pd


client = Spot(test_net_key, test_net_sekret, base_url='https://testnet.binance.vision')
#БАЛАНС АКАУНТА
print(client.account().get('balances'))
print(pd.DataFrame(client.account().get('balances')))

def wallet():
    client.user_da
"""
