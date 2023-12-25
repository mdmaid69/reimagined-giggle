import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import random
def generate_random_number(start, end):
        return random.randint(start, end)