import os
def get_current_working_directory():
        return os.getcwd()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)