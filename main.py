import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import random
def roll_die():
        return random.randint(1, 6)