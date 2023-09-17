from fp import *


def pack(array):
    def inner(array):
        def _pack(rv=None):
            if len(array) < 2:
                return pair

        return _pack

    return inner(xs)()


array = [1, 1, 1, 1, 2, 3, 3, 4, 4, 5, 5]
print(f"{pack(array)=}")
