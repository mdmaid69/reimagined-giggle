import math
def calculate_logarithm_base_e(x):
        return math.log(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)