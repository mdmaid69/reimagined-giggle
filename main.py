import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time