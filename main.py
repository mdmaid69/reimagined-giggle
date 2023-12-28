import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import platform
def get_python_version():
        return platform.python_version()