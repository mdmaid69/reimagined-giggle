import array
def get_array_as_frozenset(array):
        return frozenset(array)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])