import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)