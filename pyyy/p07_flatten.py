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


def flatten(array):
    """
    causes an inversion which needs to be reversed
    to get the correct order
    """

    def inner(pair=None):
        def _flatten(array):
            nonlocal pair
            if len(array) == 0:
                return pair

            item = array[0]
            if isinstance(item, list):
                pair = inner(Pair(item[0], pair))(item[1:])
                return inner(pair)(array[1:])

            return inner(Pair(item, pair))(array[1:])

        return _flatten

    return inner()(array)


array = [1, 2, [3, 4, 5], 6, [7, 8, [9, 10], 11], 12]

print(array)
print(list_to_array(reverse(flatten(array))))
