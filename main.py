import math
def calculate_cosine(x):
        return math.cos(x)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)