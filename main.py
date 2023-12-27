import tensorflow as tf
print(tf.__version__)
import os
def remove_directory(path):
        os.rmdir(path)