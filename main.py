def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import random
def generate_random_number(start, end):
        return random.randint(start, end)