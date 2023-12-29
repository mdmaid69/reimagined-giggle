import random
def generate_random_choice(choices):
        return random.choice(choices)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)