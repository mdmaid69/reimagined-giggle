import collections
def create_stack():
        return collections.deque()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])