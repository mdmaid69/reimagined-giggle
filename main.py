import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)