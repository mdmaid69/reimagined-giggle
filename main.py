import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height