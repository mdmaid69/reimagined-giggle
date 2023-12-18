  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import tensorflow as tf
print(tf.__version__)