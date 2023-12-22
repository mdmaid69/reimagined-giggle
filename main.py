import random
def roll_die():
        return random.randint(1, 6)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)