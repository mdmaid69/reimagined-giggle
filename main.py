import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import random
def generate_random_choice(choices):
        return random.choice(choices)