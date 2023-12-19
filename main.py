import tensorflow as tf
print(tf.__version__)
  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid