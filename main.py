import random
def roll_die():
        return random.randint(1, 6)
import os
def get_file_size(filename):
        return os.path.getsize(filename)