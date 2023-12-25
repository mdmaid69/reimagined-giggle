import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import os
def get_environment_variable(var):
        return os.getenv(var)