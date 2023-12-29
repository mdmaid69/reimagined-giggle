import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])