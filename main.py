import random
def generate_random_choice(choices):
        return random.choice(choices)
import re
def split_string(pattern, string):
        return re.split(pattern, string)