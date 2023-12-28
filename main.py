def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_sine(x):
        return math.sin(x)