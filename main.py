import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a