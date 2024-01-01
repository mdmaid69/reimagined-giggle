def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)