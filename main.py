text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}