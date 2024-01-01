import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)