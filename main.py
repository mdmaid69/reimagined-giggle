import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)