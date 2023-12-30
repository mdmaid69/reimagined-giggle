import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"