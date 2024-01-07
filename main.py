def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))