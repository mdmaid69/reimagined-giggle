import glob
def find_files(pattern):
        return glob.glob(pattern)
import tensorflow as tf
print(tf.__version__)