import random
def generate_random_choice(choices):
        return random.choice(choices)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time