import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import collections
def count_elements(iterable):
        return collections.Counter(iterable)