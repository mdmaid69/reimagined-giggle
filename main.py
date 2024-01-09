def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"