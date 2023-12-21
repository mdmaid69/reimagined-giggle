import tensorflow as tf
print(tf.__version__)
import array
def get_array_slice(array, i, j):
        return array[i:j]