from datetime import datetime
import numpy as np

text_file = open("d5.txt", "r")
lines = text_file.read().split('\n')

data0 = 'test'+lines[:-1][0]
# data = 'dabAcCaCBAcCcaDA'

count = 0

length = 10000000000

alph = 'abcdefghijkalmnoapqrstuvwxyz'

for k in alph:
    print k
    data = data0.replace(k,'').replace(k.swapcase(),'')

    res = data[0]

    for i in range(len(data)):
        if i>0:
            if data[i].swapcase() != res[-1]:
                res = res+data[i]
            else:
                res = res[:-1]

    if len(res[4:])<length:
        length = len(res[4:])
        print length



