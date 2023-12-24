import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)