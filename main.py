import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)