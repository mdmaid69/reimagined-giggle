import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3