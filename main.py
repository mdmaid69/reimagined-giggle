def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"