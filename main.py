import array
def get_array_as_bytearray(array):
        return bytearray(array)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])