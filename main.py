n = 10
print("Square numbers:", [x**2 for x in range(n)])
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a