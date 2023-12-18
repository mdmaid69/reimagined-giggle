import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))