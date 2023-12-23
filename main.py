n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)