import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list