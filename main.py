import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)