import math
def calculate_absolute_value(x):
        return math.fabs(x)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)