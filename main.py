import tensorflow as tf
print(tf.__version__)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)