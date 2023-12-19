import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)