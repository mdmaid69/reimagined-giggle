import time
def get_current_time():
        return time.time()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"