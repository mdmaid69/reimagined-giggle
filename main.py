def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))