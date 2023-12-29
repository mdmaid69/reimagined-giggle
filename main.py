import tensorflow as tf
print(tf.__version__)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)