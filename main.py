import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import math
def calculate_absolute_value(x):
        return math.fabs(x)