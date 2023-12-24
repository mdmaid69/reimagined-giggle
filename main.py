import glob
def find_files(pattern):
        return glob.glob(pattern)
import random
def generate_random_choice(choices):
        return random.choice(choices)