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


def compress(xs):
    def inner(xs):
        def _compress(pair=None):
            if xs is None:
                return pair

            if (head(xs) is not None and tail(xs) is None) or head(xs) != head(
                tail(xs)
            ):
                return inner(tail(xs))(Pair(head(xs), pair))

            return inner(tail(xs))(pair)

        return _compress

    return inner(xs)()


array = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5]
xs = array_to_list(array)
print(list_to_array(compress(xs)))

array = [1, 2, 2, 2, 3, 4, 4, 4, 5, 5]
xs = array_to_list(array)
print(list_to_array(compress(xs)))
