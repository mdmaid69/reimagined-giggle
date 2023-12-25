import random
def generate_random_number(start, end):
        return random.randint(start, end)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)