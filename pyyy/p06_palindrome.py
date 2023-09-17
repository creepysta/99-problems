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


def is_eq(xs):
    def inner(other):
        if xs is None and other is None:
            return True
        if xs is None or other is None:
            return False
        if head(xs) != head(other):
            return False

        return is_eq(tail(xs))(tail(other))

    return inner


def is_palindrome(xs):
    rev = reverse(xs)
    return is_eq(xs)(rev)


xs = array_to_list([2, 3, 4, 3, 2])
print(is_palindrome(xs))

xs = array_to_list([2, 3, 3, 2])
print(is_palindrome(xs))

print(is_palindrome(range(1)(5)))
