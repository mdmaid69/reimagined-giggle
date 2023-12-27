import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list