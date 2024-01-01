import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a