import tensorflow as tf
print(tf.__version__)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)