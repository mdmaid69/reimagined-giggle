import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_perpetuity(payment, rate):
        return payment / rate