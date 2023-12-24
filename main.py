import math
def calculate_factorial(n):
        return math.factorial(n)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)