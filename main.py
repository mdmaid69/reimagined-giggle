  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import tensorflow as tf
print(tf.__version__)