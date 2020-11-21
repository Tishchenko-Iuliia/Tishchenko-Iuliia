a1, a2 = map(int, input().split())


def gcd(rest1, rest2):
    if rest1 == 0:
        return (rest2, 0, 1)
    z, x, y = gcd(rest2 % rest1, rest1)
    return(z, y - (rest2 // rest1) * x, x)

d = gcd(a1, a2)
print(f' {d[0]} = {str(a1)}*{d[1]}+{str(a2)}*{d[2]}')
