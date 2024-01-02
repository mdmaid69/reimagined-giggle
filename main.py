import random
def generate_random_number(start, end):
        return random.randint(start, end)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)