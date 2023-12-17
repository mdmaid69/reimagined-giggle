import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)