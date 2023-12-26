import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)