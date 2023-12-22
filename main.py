import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))