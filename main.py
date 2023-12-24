import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)