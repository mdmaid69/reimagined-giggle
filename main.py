import tensorflow as tf
print(tf.__version__)
import array
def get_array_as_memoryview(array):
        return memoryview(array)