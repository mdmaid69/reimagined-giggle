import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import platform
def get_python_version():
        return platform.python_version()