import tensorflow as tf
print(tf.__version__)
import os
def change_working_directory(path):
        os.chdir(path)