import array
def get_list_from_array(array):
        return array.tolist()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])