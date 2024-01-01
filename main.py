import math
def calculate_factorial(n):
        return math.factorial(n)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)