import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import itertools
print(list(itertools.permutations([1, 2, 3])))