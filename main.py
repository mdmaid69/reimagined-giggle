text = "Hello, world!"
print("Characters:", len(text))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)