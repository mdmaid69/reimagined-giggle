import tensorflow as tf
print(tf.__version__)
import glob
def find_files(pattern):
        return glob.glob(pattern)