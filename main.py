import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)