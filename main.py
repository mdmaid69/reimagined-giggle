def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"