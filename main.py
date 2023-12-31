import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)