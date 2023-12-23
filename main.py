import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list