import time
def get_time_since_epoch():
        return time.time()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"