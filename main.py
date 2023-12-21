import tensorflow as tf
print(tf.__version__)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)