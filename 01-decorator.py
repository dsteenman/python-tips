from time import time


def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print(f'elasped: {after - before}')
        return rv
    return f


@timer
def add(x, y, z):
    return x + y + z


print(add(5, 5, 5))
