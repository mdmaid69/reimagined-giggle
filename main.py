import os
def change_working_directory(path):
        os.chdir(path)
import random
def roll_die():
        return random.randint(1, 6)