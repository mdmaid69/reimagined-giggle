def calculate_roi(gain, cost):
        return (gain - cost) / cost
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"