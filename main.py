import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)