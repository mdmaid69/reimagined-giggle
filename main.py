text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import array
def get_array_buffer_info(array):
        return array.buffer_info()