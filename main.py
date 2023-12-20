import array
def convert_array_to_list(array):
        return array.tolist()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])