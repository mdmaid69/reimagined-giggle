text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)