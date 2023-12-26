import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a