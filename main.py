import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import random
def generate_random_choice(choices):
        return random.choice(choices)