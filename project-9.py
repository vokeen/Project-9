import os
from os import system
import random
system('clear')

seq=[1,1]
while True:
    x = seq[-2]
    y = seq[-1]
    num = x+y
    seq.append(num)
    if num > 1000:
        print(seq)
        break
