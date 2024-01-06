import glob
def find_files(pattern):
        return glob.glob(pattern)
import random
def generate_random_number(start, end):
        return random.randint(start, end)