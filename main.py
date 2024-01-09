text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)