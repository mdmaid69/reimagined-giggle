def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"