import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)