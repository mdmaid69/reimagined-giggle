import tensorflow as tf
print(tf.__version__)
  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime