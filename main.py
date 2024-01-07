import math
def calculate_circle_area(radius):
        return math.pi * radius**2
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)