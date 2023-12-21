import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a