import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from connectiontoAPI import *

config_logging(logging, logging.DEBUG)

client = Client(key=test_net_key, secret=test_net_sekret)