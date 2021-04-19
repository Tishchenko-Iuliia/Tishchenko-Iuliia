from math import sqrt, ceil

def is_simple(value):
    if value in [2,3]:
        return True
    elif value%2 != 0:
        for i in range(3, ceil(sqrt(value))+1, 2):
            if value%i == 0:
                return False
        return True
    return False

