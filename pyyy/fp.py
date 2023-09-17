"""
https://v2.ocaml.org/learn/tutorials/99problems.html
"""


from collections import namedtuple

Pair = namedtuple("Pair", ["first", "second"])


def pair(x):
    def fn(y):
        return Pair(x, y)

    return fn


def head(pair):
    return pair.first


def tail(pair):
    return pair.second


def range(left):
    def fn(right):
        if left > right:
            return None
        return Pair(left, range(left + 1)(right))

    return fn


# impure because mutates nonlocal array
def list_to_array(xs):
    rv = []

    def inner(xs):
        nonlocal rv
        if xs is None:
            return rv
        rv.append(head(xs))
        return inner(tail(xs))

    return inner(xs)


# impure since accepts array?
def array_to_list(array):
    def inner(array):
        def _inner(rv=None):
            if len(array) == 0:
                return rv
            return inner(array[1:])(Pair(array[0], rv))

        return _inner

    return inner(array)()


def mmap(func):
    def inner(xs):
        if xs is None:
            return None
        return Pair(func(head(xs)), mmap(func)(tail(xs)))

    return inner


def inf_curry(arg=None):
    items = []

    def inner(a=None):
        nonlocal items
        if a is None:
            return items

        items.append(a)
        return inner

    return inner(arg)


def mfilter(func):
    def inner(xs):
        if xs is None:
            return None
        if func(head(xs)) is True:
            return Pair(head(xs), mfilter(func)(tail(xs)))

        return mfilter(func)(tail(xs))

    return inner


def take(xs):
    def inner(n):
        if n <= 0:
            return None
        return Pair(head(xs), take(tail(xs))(n - 1))

    return inner


def sieve(xs):
    """
    ref - https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """
    if xs is None:
        return None

    return Pair(head(xs), sieve(mfilter(lambda x: x % head(xs) != 0)(tail(xs))))


def mersenne(xs):
    """
    https://en.wikipedia.org/wiki/Mersenne_prime
    mersenne primes - any prime of the form 2**n - 1
    """
    if xs is None:
        return None

    return Pair(head(xs), mersenne(mfilter(lambda x: x & (x + 1) == 0)(tail(xs))))


def fold_left(func):
    def fold(xs):
        def accm(acc):
            if xs is None:
                return acc

            return fold(tail(xs))(func(head(xs), acc))

        return accm

    return fold


def reduce(func):
    acc = None

    def _reduce(xs):
        nonlocal acc
        if xs is None:
            return acc
        if acc is None:
            acc = 0  # head(xs)

        return fold_left(func)(xs)(acc)

    return _reduce


# TODO: maybe actually make the `Pair` lazy where the tail is itself
# a function which needs to be called to be evaluated.
