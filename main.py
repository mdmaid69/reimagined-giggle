import math
def calculate_square_root(x):
        return math.sqrt(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a