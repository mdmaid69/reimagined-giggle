  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import tensorflow as tf
print(tf.__version__)