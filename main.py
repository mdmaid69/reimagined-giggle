import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time