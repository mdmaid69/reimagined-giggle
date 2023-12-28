import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import math
def calculate_circle_area(radius):
        return math.pi * radius**2