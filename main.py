text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable