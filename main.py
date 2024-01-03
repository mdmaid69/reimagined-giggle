import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time