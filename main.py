import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import glob
def find_files(pattern):
        return glob.glob(pattern)