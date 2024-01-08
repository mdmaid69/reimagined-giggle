import shutil
def delete_directory(path):
        shutil.rmtree(path)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)