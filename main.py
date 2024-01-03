import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import math
def calculate_sign(x):
        return math.copysign(1, x)