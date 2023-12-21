n = 10
print("Powers of 2:", [2**x for x in range(n)])
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a