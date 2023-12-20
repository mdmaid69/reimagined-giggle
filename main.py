import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)