from CallBack import *
from DataSets import *

def toFixed(num, digits=0):
    return num * 10**digits // 1 / 10**digits

#set_coin_filters()

def characters_after_the_period(word):
    num = 0
    for i in range(0, len(word)):
        if word[i] == '0':
            num += 1
        if word[i] == '1':
            return num

print(characters_after_the_period('1.0000'))