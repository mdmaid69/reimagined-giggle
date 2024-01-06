import tensorflow as tf
print(tf.__version__)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)