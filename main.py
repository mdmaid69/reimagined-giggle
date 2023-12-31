import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)