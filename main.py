  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import tensorflow as tf
print(tf.__version__)