import array
def get_array_slice(array, i, j):
        return array[i:j]
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])