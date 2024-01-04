import math
def calculate_arc_cosine(x):
        return math.acos(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a