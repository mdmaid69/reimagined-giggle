import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import os
def change_working_directory(path):
        os.chdir(path)