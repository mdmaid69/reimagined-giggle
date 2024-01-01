import array
def extend_array(array, iterable):
        array.extend(iterable)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])