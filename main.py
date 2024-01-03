import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_density(mass, volume):
        return mass / volume