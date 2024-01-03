import math
def calculate_cosine(x):
        return math.cos(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a