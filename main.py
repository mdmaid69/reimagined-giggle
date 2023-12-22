  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import tensorflow as tf
print(tf.__version__)