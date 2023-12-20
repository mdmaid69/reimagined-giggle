text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))