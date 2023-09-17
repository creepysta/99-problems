from fp import *


def last(xs):
    if xs is None:
        return None
    if tail(xs) is None:
        return head(xs)
    return last(tail(xs))


print(last(range(1)(100)))
