import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
name = "Python"
print("Hello,", name)