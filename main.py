import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height