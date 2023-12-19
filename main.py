import os
def get_file_size(filename):
        return os.path.getsize(filename)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"