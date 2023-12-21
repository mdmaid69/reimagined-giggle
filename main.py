import tensorflow as tf
print(tf.__version__)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)