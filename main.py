import math
def calculate_factorial(n):
        return math.factorial(n)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)