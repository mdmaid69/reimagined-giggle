def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height