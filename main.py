import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)