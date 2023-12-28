import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"