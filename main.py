import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list