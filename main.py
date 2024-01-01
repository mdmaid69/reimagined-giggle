import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import tensorflow as tf
print(tf.__version__)