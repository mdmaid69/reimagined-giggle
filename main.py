import math
def calculate_factorial(n):
        return math.factorial(n)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a