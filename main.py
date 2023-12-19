import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import shutil
def delete_directory(path):
        shutil.rmtree(path)