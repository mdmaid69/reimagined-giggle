n = 10
print("Powers of 2:", [2**x for x in range(n)])
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a