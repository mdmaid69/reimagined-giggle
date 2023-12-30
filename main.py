import math
def calculate_gamma_function(x):
        return math.gamma(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)