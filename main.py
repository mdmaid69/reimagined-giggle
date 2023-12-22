import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)