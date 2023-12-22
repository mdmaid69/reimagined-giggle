import math
def calculate_exponential(x):
        return math.exp(x)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a