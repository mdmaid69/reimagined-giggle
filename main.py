import random
def generate_random_choice(choices):
        return random.choice(choices)
import os
def list_files_in_directory(path):
        return os.listdir(path)