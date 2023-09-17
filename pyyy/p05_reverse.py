from fp import *


def reverse(xs):
    """
    return nth element of a zero index array
    """

    def inner(pair):
        def _rev(xs):
            if xs is None:
                return pair

            return inner(Pair(head(xs), pair))(tail(xs))

        return _rev

    return inner(None)(xs)


print(list_to_array(reverse(range(1)(100))))
