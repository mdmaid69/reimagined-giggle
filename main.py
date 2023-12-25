import random
def generate_random_choice(choices):
        return random.choice(choices)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)