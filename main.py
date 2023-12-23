import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2