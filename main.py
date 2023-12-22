n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a