import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b