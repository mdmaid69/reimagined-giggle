import random
def generate_random_choice(choices):
        return random.choice(choices)
import os
def get_file_size(filename):
        return os.path.getsize(filename)