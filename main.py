import tensorflow as tf
print(tf.__version__)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)