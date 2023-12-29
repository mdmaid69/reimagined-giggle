import random
def generate_random_choice(choices):
        return random.choice(choices)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)