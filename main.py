import random
def roll_die():
        return random.randint(1, 6)
import glob
def find_files(pattern):
        return glob.glob(pattern)