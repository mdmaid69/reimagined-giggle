import tensorflow as tf
print(tf.__version__)
import shutil
def delete_directory(path):
        shutil.rmtree(path)