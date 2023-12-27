import glob
def find_files(pattern):
        return glob.glob(pattern)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list