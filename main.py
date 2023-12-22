import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)