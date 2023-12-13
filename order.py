from binance.spot import Spot
from connectiontoAPI import *


client = Spot(test_net_key, test_net_sekret, base_url='https://testnet.binance.vision')

def toFixed1(num, digits=0):
    return num * 10**digits // 1 / 10**digits



def open_new_order(B_BorA, coin_pair):
    B_BorA_P, B_BorA_CN, B_BorA_Q, type = B_BorA[0], B_BorA[1], B_BorA[2], B_BorA[3]
    if type == 'BUY':
        a = coin_pair[0]
    elif type == 'SELL':
        a = coin_pair[1]
    """кількісний показник ордера - проблема"""
    params = {
        'symbol': B_BorA_CN,
        'side': type,
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': 0.002, #проблема
        'price': B_BorA_P
    }
    #відкриття ордера
    client.new_order(**params)

#закрить ордер
#response = client.cancel_open_orders('BTCUSDT')


#ІСТОРІЯ ОРДЕРІВ

"""df = pd.DataFrame(
    client.get_orders(symbol = 'BTCUSDT'),
    columns=['orderId', 'type', 'side', 'price', 'status']
)"""

print(df.tail(15))
