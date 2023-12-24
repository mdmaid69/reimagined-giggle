n = 10
print("Square numbers:", [x**2 for x in range(n)])
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a