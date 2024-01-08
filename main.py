import tensorflow as tf
print(tf.__version__)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)