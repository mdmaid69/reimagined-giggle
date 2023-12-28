import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))