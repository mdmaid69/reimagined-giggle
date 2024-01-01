import math
def calculate_circle_area(radius):
        return math.pi * radius**2
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)