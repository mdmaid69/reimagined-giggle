import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import random
def generate_random_number(start, end):
        return random.randint(start, end)