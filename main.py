import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a