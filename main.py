import random
def roll_die():
        return random.randint(1, 6)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time