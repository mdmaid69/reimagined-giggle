import collections
def create_queue():
        return collections.deque()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])