import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import os
def remove_directory(path):
        os.rmdir(path)