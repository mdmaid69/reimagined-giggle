text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import array
def get_array_as_frozenset(array):
        return frozenset(array)