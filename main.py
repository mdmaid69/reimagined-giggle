import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_area_circle(r):
        return 3.14 * r**2