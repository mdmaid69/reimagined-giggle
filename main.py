import array
def convert_array_to_bytes(array):
        return array.tobytes()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])