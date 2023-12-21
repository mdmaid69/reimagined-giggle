i = 0
while i < 5:
        print(i)
        i += 1
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a