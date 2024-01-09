text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import collections
def count_elements(iterable):
        return collections.Counter(iterable)