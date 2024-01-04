import random
def generate_random_choice(choices):
        return random.choice(choices)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)