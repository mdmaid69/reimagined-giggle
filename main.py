import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))