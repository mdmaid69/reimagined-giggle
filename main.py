import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import random
def roll_die():
        return random.randint(1, 6)