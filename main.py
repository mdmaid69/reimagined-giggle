import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import tensorflow as tf
print(tf.__version__)