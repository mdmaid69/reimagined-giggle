text = "Hello, world!"
print("Words:", len(text.split()))
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a