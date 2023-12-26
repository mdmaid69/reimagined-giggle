import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2