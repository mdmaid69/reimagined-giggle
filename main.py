import random
def roll_die():
        return random.randint(1, 6)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)