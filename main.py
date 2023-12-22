import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))