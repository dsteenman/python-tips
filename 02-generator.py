# top-level syntax, function -> underscore method
#    x()                __call__
from time import sleep


def compute():
    for i in range(10):
        sleep(.5)
        yield i


for val in compute():
    print(val)
