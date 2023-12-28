import array
def get_array_as_repr(array):
        return repr(array)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])