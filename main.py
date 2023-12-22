import tensorflow as tf
print(tf.__version__)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)