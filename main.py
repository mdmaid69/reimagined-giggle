import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_pressure(force, area):
        return force / area