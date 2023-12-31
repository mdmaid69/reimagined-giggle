def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)