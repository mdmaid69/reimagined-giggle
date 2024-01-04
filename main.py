import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])