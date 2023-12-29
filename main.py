import array
def get_array_as_tuple(array):
        return tuple(array)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])