import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)