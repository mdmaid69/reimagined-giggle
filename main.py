text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)