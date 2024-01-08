import os
def get_file_size(filename):
        return os.path.getsize(filename)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height