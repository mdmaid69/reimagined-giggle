import math
def calculate_cosine(x):
        return math.cos(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a