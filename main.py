text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)