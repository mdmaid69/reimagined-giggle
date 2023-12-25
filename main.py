def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height