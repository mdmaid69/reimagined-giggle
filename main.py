  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import tensorflow as tf
print(tf.__version__)