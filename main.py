import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import random
def roll_die():
        return random.randint(1, 6)