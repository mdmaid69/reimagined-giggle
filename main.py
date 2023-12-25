import array
def get_string_from_array(array):
        return array.tobytes()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])