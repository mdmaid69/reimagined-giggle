x = 10
y = 20
print("Sum:", x + y)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a