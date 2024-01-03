import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)