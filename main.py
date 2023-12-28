import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time