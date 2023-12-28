import shutil
def delete_directory(path):
        shutil.rmtree(path)
import random
def generate_random_choice(choices):
        return random.choice(choices)