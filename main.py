import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_pressure(force, area):
        return force / area