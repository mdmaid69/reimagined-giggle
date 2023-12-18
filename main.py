text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))