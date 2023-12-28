import array
def convert_array_to_unicode(array):
        return array.tounicode()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])