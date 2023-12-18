import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)