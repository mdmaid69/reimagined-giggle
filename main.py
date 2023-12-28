import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time