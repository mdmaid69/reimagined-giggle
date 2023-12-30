def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)