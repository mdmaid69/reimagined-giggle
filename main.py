import collections
def create_counter():
        return collections.Counter()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])