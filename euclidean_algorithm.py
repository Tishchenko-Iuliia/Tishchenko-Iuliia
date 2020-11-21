
a,b=map(int,input().split())

def gcd(a,b):
    rest2 = min(a,b)
    rest1 = max(a,b)
    rest3 = rest1 % rest2
    while rest3 != 0:
        rest1 = rest2
        rest2 = rest3
        rest3 = rest1 % rest2

    return rest2

print(gcd(a,b))
