text = "Hello, world!"
print("Words:", len(text.split()))
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a