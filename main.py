import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)