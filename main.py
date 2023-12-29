import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)