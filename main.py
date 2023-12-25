import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import os
def remove_directory(path):
        os.rmdir(path)