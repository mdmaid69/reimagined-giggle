import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius