import random
def roll_die():
        return random.randint(1, 6)
import os
def list_files_in_directory(path):
        return os.listdir(path)