import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import random
def roll_die():
        return random.randint(1, 6)