import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"