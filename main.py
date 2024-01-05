import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])