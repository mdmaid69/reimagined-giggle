def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)