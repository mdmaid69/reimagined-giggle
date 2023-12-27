import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)