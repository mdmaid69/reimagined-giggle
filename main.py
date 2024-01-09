import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)