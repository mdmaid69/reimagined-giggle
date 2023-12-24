import math
def calculate_absolute_value(x):
        return math.fabs(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a