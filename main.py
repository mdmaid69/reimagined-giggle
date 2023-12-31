def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import random
def generate_random_choice(choices):
        return random.choice(choices)