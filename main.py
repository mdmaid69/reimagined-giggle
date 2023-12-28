import array
def insert_into_array(array, i, item):
        array.insert(i, item)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])