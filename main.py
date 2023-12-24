import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))