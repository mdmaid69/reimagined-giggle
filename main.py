import tensorflow as tf
print(tf.__version__)
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize