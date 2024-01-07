import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a