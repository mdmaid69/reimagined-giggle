import math
def calculate_ceiling(x):
        return math.ceil(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a