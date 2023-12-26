import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import os
def change_working_directory(path):
        os.chdir(path)