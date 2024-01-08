numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a