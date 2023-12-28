  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import tensorflow as tf
print(tf.__version__)