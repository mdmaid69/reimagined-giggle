import tensorflow as tf
print(tf.__version__)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)