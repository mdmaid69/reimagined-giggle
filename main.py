import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])