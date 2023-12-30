text = "Hello, world!"
print("Words:", len(text.split()))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)