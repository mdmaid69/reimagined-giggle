import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)