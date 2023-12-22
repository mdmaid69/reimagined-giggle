import random
def generate_random_number(start, end):
        return random.randint(start, end)
import os
def list_files_in_directory(path):
        return os.listdir(path)