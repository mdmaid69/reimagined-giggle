import random
def roll_die():
        return random.randint(1, 6)
import shutil
def delete_directory(path):
        shutil.rmtree(path)