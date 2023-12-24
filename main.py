  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import tensorflow as tf
print(tf.__version__)