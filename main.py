import random
def generate_random_choice(choices):
        return random.choice(choices)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)