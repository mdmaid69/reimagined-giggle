import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"