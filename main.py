import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import random
def roll_die():
        return random.randint(1, 6)