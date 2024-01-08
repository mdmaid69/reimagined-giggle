import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))