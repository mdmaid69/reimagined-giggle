import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)