import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a