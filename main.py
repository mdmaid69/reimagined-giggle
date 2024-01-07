import re
def split_string(pattern, string):
        return re.split(pattern, string)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"