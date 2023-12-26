def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3