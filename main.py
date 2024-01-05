import sys
def add_to_python_path(path):
        sys.path.append(path)
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)