import array
def convert_array_to_string(array):
        return array.tostring()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])