import random
def generate_random_choice(choices):
        return random.choice(choices)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time