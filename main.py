import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import math
def calculate_sign(x):
        return math.copysign(1, x)