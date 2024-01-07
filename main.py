import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import random
def roll_die():
        return random.randint(1, 6)