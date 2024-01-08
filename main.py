import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
x = 10
y = 20
print("Sum:", x + y)