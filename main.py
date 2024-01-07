def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)