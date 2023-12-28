import os
def remove_directory(path):
        os.rmdir(path)
import random
def roll_die():
        return random.randint(1, 6)