import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import math
def calculate_circle_area(radius):
        return math.pi * radius**2