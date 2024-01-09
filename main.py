import collections
def create_ordered_dict():
        return collections.OrderedDict()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])