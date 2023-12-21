import tensorflow as tf
print(tf.__version__)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)