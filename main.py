numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a