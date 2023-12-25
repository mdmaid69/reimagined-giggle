import tensorflow as tf
print(tf.__version__)
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen