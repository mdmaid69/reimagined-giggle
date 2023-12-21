import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])