import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a