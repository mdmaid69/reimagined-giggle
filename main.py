import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)