from fp import *


def kth(xs):
    """
    return kth element of a zero index array
    """

    def inner(k):
        if xs is None:
            raise IndexError("not enough elements to unpack")

        if k == 0:
            return head(xs)

        return kth(tail(xs))(k - 1)

    return inner


print(kth(range(1)(100))(4))
