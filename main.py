import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])