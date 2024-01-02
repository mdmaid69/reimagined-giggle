import math
def calculate_square_root(x):
        return math.sqrt(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a