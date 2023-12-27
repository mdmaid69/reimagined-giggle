import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)