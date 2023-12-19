import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time