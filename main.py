  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import tensorflow as tf
print(tf.__version__)