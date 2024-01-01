import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a