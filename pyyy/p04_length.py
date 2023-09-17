from fp import *


def length(xs):
    """
    return nth element of a zero index array
    """

    def inner(n):
        def _length(xs):
            if xs is None:
                return n

            return inner(n + 1)(tail(xs))

        return _length

    return inner(0)(xs)


print(length(range(1)(100)))
