import sys
from random import random
from operator import add
def f(_):
    x = random() * 2 - 1
    y = random() * 2 - 1
    return 1 if x ** 2 + y ** 2 < 1 else 0

def main(sc):
    slices = 200
    n = 1000000 * slices
    count = sc.parallelize(xrange(1, n+1), slices).map(f).reduce(add)
    print "%f" % (4.0 * count / n)