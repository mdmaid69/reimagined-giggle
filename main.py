import tensorflow as tf
print(tf.__version__)
import os
def list_files_in_directory(path):
        return os.listdir(path)