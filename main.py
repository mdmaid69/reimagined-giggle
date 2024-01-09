import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_force(mass, acceleration):
        return mass * acceleration