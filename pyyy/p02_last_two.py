from fp import *


def last_two(xs):
    if xs is None or tail(xs) is None:
        return None

    if tail(tail(xs)) is None:
        return head(xs), head(tail(xs))

    return last_two(tail(xs))


print(last_two(range(1)(100)))
