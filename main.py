import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a