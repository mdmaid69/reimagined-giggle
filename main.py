import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)