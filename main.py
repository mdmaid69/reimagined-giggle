import tensorflow as tf
print(tf.__version__)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)