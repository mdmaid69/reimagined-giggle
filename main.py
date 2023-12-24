import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))