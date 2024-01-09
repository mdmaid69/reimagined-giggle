import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)