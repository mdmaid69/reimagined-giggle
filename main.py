import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)