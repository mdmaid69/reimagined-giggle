import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])