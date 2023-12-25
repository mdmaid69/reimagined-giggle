import random
def roll_die():
        return random.randint(1, 6)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)