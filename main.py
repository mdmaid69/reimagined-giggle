import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2