import os
def list_files_in_directory(path):
        return os.listdir(path)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"