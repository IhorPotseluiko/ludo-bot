from DataSets import *
from Clientik import *

def message_handler(message):
    mark_c = str(message.get('s'))
    if mark_c != 'None':
        coin, bbidprice, bbidqty, baskprice, baskqty = 'coin', 'bbidprice','bbidqty', 'baskprice', 'baskqty'
        coin, bbidprice, bbidqty, baskprice, baskqty = coin + mark_c, bbidprice + mark_c, bbidqty + mark_c, baskprice + mark_c, baskqty + mark_c
        DataBookTickerRealTime.set(coin, message.get('s'))
        DataBookTickerRealTime.set(bbidprice, message.get('b'))
        DataBookTickerRealTime.set(bbidqty, message.get('B'))
        DataBookTickerRealTime.set(baskprice, message.get('a'))
        DataBookTickerRealTime.set(baskqty, message.get('A'))

def set_coin_filters():
    print("запускаєм запрос")
    dataset = client.exchange_info()
    for i in range(0, len(dataset.get('symbols'))):
        filters = dataset.get('symbols')[i].get('filters')
        coin = dataset.get('symbols')[i].get('symbol')
        DataCoinFilters.set('filters' + coin, filters)
