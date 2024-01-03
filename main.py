def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))