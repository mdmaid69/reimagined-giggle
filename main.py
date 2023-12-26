import random
def generate_random_number(start, end):
        return random.randint(start, end)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)