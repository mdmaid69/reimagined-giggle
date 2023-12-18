import tensorflow as tf
print(tf.__version__)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))