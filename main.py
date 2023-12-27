def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_logarithm_base_10(x):
        return math.log10(x)