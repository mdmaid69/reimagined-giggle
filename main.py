import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time