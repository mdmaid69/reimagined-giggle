import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list