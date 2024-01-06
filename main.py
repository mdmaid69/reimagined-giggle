import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)