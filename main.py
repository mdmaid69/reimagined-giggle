import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)