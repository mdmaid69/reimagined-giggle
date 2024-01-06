import math
def calculate_floor(x):
        return math.floor(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a