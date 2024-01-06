import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())