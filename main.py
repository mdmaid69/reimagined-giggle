import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def greet(name):
        print(f"Hello, {name}!")