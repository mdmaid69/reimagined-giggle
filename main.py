import random
def roll_die():
        return random.randint(1, 6)
import os
def remove_directory(path):
        os.rmdir(path)