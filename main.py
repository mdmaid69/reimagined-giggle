import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list