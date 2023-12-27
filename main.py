import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)