import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import shutil
def move_file(src, dst):
        shutil.move(src, dst)