import glob
def find_files(pattern):
        return glob.glob(pattern)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"