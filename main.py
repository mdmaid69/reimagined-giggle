import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"