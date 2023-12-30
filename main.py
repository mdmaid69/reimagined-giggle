import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a