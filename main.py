import re
def split_string(pattern, string):
        return re.split(pattern, string)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)