import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import shutil
def delete_directory(path):
        shutil.rmtree(path)