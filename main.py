import tensorflow as tf
print(tf.__version__)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))