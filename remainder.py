from math import sqrt, ceil
from numbers import Number

def is_simple(mod):
    if mod in [2,3]:
        return True
    elif mod%2 != 0:
        for i in range(3, ceil(sqrt(mod))+1, 2):
            if mod%i == 0:
                return False
        return True
    return False

class RemainderDomainError(ValueError):
    pass

class Remainder:
    """Остатки по модулю"""

    def __init__(self, arg=0):
        """r -- число"""
        if isinstance( arg ,Number):
            self.r = arg % mod
        else:
            raise RemainderDomainError( "You are trying to create remainder from " + repr(arg))

    def __str__(self):
        return str(self.r)

    def __eq__(self, other):
        if isinstance( other,Number):
            other = Remainder

        if isinstance(other, Remainder):
            return self.r == other.r
        else:
            raise RemainderDomainError("Can`t say if remainder is equal to" + str(type(other)))

    def __add__(self, other):
        if isinstance( other,Number):
            other = Remainder(other)

        return Remainder(self.r+other.r)

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Remainder(mod - self.r)

    def __sub__(self, other):
        if isinstance(other, Number):
            other = Remainder(other)

        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        if isinstance(other, Number):
            other = Remainder(other)

        return Remainder( self.r*other.r % mod )

    def __rmul__(self, other):
        return self.__mul__(other)



mod=13

r1=Remainder(5)
r2=Remainder(34)
r3=Remainder(21)

print(r1,r2)
print(r1==r2)
print(r1+r2)
print(r1-r3)
print(r1*r2)
print(r1*r2+r3)
