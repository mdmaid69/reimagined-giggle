import itertools
print(list(itertools.permutations([1, 2, 3])))
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a