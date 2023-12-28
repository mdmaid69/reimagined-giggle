import tensorflow as tf
print(tf.__version__)
import os
def get_file_size(filename):
        return os.path.getsize(filename)