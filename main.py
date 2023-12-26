import array
def set_array_item(array, i, item):
        array[i] = item
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])