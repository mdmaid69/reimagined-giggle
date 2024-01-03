import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_density(mass, volume):
        return mass / volume