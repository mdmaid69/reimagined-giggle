def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)