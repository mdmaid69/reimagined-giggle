def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)