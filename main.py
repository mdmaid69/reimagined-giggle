import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable