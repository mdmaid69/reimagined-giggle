import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)