def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))