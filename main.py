import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_force(mass, acceleration):
        return mass * acceleration