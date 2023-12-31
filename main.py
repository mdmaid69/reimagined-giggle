import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)