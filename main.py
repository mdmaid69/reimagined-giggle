import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import os
def remove_directory(path):
        os.rmdir(path)