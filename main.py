def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))