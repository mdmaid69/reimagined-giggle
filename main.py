import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import random
def generate_random_choice(choices):
        return random.choice(choices)