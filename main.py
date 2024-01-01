import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)