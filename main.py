import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])