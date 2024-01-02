import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list