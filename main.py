import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import tensorflow as tf
print(tf.__version__)