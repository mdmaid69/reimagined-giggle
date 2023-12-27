import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import random
def roll_die():
        return random.randint(1, 6)