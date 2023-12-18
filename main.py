import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a