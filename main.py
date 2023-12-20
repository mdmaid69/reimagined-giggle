import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import tensorflow as tf
print(tf.__version__)