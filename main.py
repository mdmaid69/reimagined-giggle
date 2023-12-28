text = "Hello, world!"
print("Reversed:", text[::-1])
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a