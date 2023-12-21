import tensorflow as tf
print(tf.__version__)
import array
def get_array_as_frozenset(array):
        return frozenset(array)