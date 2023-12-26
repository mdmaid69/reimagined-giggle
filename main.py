def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import random
def roll_die():
        return random.randint(1, 6)