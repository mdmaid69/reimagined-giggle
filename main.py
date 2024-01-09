import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import random
def generate_random_number(start, end):
        return random.randint(start, end)