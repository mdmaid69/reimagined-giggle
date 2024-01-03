import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list