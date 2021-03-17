import random
import time
import sys
import multiprocessing
from matplotlib import pyplot as pp


def sum_randoms(n):
    ran = random.Random()

    item = 0
    for i in range(n):
        item += ran.random()

    return item


def test_all(pool):
    l = pool.map(sum_randoms, [10000] * 50)
    pp.plot(l)
    pp.show()
    return l


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(test_all(pool))
    print("Time spent:", time.time() - t0)
else:
    print(__name__)
