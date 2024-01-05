import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import random
def roll_die():
        return random.randint(1, 6)