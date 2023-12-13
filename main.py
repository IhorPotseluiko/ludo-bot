import time
import logging
from binance.lib.utils import config_logging
from binance.websocket.spot.websocket_client import SpotWebsocketClient
from algorithm import *
from CallBack import *
from connectiontoAPI import *
import sys
#from test import AlgorithmOfProfit

config_logging(logging, logging.DEBUG)
""" створення екземпляру класа LastPrice пыд назвою DataSpot"""
def tracking_book_ticker(a):
    my_client.book_ticker(
        symbol=a,
        id=1,
        callback=message_handler,
    )

def tracking_book_ticker1():
    my_client.book_ticker(
        id=1,
        callback=message_handler,
    )


timeout = time.time() + 35 # +5
if __name__ == "__main__":
    """ перевірка рахунку: дані комісій, спотовий баланс"""
    my_client = SpotWebsocketClient()
    my_client.start()
    set_coin_filters()
    print(DataCoinFilters.check())
    time.sleep(5)
    """ відслідковування змін на споті з допомогою user_data і запис в екземпляр класу LastPrice - DataSpot"""
    tracking_book_ticker1()
    while True:
        Algoritm_OF_profit()
        time.sleep(0.1)
        if time.time() > timeout:
            break
    logging.debug("closing ws connection")
    print("python hueta do", my_client.is_alive())
    #print("ctroka ", my_client.)
    my_client.stop()
    time.sleep(5)
    print("python hueta posle", my_client.is_alive())
    #print(lastprice.items())
    print("конец")

