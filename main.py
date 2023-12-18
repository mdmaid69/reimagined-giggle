import array
def get_array_as_bool(array):
        return bool(array)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])