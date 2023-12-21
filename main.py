import os
def change_working_directory(path):
        os.chdir(path)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)