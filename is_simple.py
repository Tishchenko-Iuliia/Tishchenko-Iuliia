from math import sqrt, ceil
import random

a=int(input())
n=0

def is_simple(value):
    global n
    if value == 2 or value == 3:
        return True
    elif value%2 != 0:
        for i in range(3, ceil(sqrt(value))+1, 2):
            if value%i == 0:
                n += 1
        if n==0:
            return True
    return False

print( is_simple(a))

def fermat(value):
    for i in range(30):
        b=random.Random().randint(2,value - 1)
        for j in range(2, value - 1):
            b = b**j % value
        if b==1:
            return True
        return False

print(fermat(a))
