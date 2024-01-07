import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)