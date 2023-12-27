text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a