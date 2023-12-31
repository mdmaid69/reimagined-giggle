def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)