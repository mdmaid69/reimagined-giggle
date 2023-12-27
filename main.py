import re
def split_string(pattern, string):
        return re.split(pattern, string)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)