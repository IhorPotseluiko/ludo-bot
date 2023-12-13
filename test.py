from datetime import time

DataCoinFilters = {'filterOPUSDT': [{'filterType': 'PRICE_FILTER', 'minPrice': '0.00100000', 'maxPrice': '1000.00000000', 'tickSize': '0.00100000'}, {'filterType': 'PERCENT_PRICE', 'multiplierUp': '5', 'multiplierDown': '0.2', 'avgPriceMins': 5}, {'filterType': 'LOT_SIZE', 'minQty': '0.01000000', 'maxQty': '92141578.00000000', 'stepSize': '0.01000000'}, {'filterType': 'MIN_NOTIONAL', 'minNotional': '10.00000000', 'applyToMarket': True, 'avgPriceMins': 5}, {'filterType': 'ICEBERG_PARTS', 'limit': 10}, {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '1593553.08332177', 'stepSize': '0.00000000'}, {'filterType': 'TRAILING_DELTA', 'minTrailingAboveDelta': 10, 'maxTrailingAboveDelta': 2000, 'minTrailingBelowDelta': 10, 'maxTrailingBelowDelta': 2000}, {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}], 'filterOPBTC': [{'filterType': 'PRICE_FILTER', 'minPrice': '0.00000001', 'maxPrice': '1000.00000000', 'tickSize': '0.00000001'}, {'filterType': 'PERCENT_PRICE', 'multiplierUp': '5', 'multiplierDown': '0.2', 'avgPriceMins': 5}, {'filterType': 'LOT_SIZE', 'minQty': '0.01000000', 'maxQty': '92141578.00000000', 'stepSize': '0.01000000'}, {'filterType': 'MIN_NOTIONAL', 'minNotional': '0.00010000', 'applyToMarket': True, 'avgPriceMins': 5}, {'filterType': 'ICEBERG_PARTS', 'limit': 10}, {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '65081.15309722', 'stepSize': '0.00000000'}, {'filterType': 'TRAILING_DELTA', 'minTrailingAboveDelta': 10, 'maxTrailingAboveDelta': 2000, 'minTrailingBelowDelta': 10, 'maxTrailingBelowDelta': 2000}, {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}], 'filterBTCBUSD': [{'filterType': 'PRICE_FILTER', 'minPrice': '0.01000000', 'maxPrice': '1000000.00000000', 'tickSize': '0.01000000'}, {'filterType': 'PERCENT_PRICE', 'multiplierUp': '5', 'multiplierDown': '0.2', 'avgPriceMins': 5}, {'filterType': 'LOT_SIZE', 'minQty': '0.00001000', 'maxQty': '9000.00000000', 'stepSize': '0.00001000'}, {'filterType': 'MIN_NOTIONAL', 'minNotional': '10.00000000', 'applyToMarket': True, 'avgPriceMins': 5}, {'filterType': 'ICEBERG_PARTS', 'limit': 10}, {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '117.52927735', 'stepSize': '0.00000000'}, {'filterType': 'TRAILING_DELTA', 'minTrailingAboveDelta': 10, 'maxTrailingAboveDelta': 2000, 'minTrailingBelowDelta': 10, 'maxTrailingBelowDelta': 2000}, {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}]}
DataForTheTransaction = {'exit_coin_couple': 'OPUSDT', 'the_exit_number_of_coins_bought': 41.805433829973715, 'best_exit_price': 2.129, 'exit_PaymentMethod': 'BUY', 'exit_availability_check_coin': 'OP', 'average_coin_couple': 'OPBTC', 'the_average_number_of_coins_bought': 0.0038160000000000004, 'best_average_price': 9.128e-05, 'average_PaymentMethod': 'SELL', 'average_availability_check_coin': 'BTC', 'out_coin_couple': 'BTCBUSD', 'the_out_number_of_coins_bought': 88.62686712000001, 'best_out_price': 23225.07, 'out_PaymentMethod': 'SELL', 'out_availability_check_coin': 'BUSD'}


zxc1 = {'best_price': 2.129, 'best_qty': 655.91, 'coin_couple': 'OPUSDT', 'PaymentMethod': 'BUY', 'coin1': 'OP', 'coin2': 'USDT'}
zxc2 = {'coin_couple': 'OPBTC', 'best_price': 9.128e-05, 'best_qty': 235.51, 'coin1': 'BTC', 'coin2': 'OP', 'PaymentMethod': 'SELL'}
zxc3 = {'best_price': 23225.07, 'best_qty': 0.01908, 'coin_couple': 'BTCBUSD', 'coin1': 'BUSD', 'coin2': 'BTC', 'PaymentMethod': 'SELL'}
import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from connectiontoAPI import *
import pandas as pd
from binance.websocket.spot.websocket_client import SpotWebsocketClient

def message_handler(message):
    print("работаєм 1 ", message)



config_logging(logging, logging.DEBUG)

client = Client(key=test_net_key, secret=test_net_sekret, base_url="https://testnet.binance.vision")

response = client.new_listen_key()
ws_client = SpotWebsocketClient(stream_url="wss://testnet.binance.vision")

ws_client.start()

print(pd.DataFrame(client.account().get('balances')))


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

new_order('BTCUSDT', 'BUY', 0.1, 23000)
print(pd.DataFrame(client.account().get('balances')))

new_order('BTCUSDT', 'SELL', 0.1, 19000)
print(pd.DataFrame(client.account().get('balances')))

time.sleep(5)

logging.debug("closing ws connection")
ws_client.stop()