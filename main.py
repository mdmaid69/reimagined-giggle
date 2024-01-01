import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)