def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import random
def roll_die():
        return random.randint(1, 6)