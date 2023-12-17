import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius