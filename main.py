  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import tensorflow as tf
print(tf.__version__)