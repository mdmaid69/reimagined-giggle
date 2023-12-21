import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3