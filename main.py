import itertools
print(list(itertools.permutations([1, 2, 3])))
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])