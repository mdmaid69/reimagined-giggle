import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)