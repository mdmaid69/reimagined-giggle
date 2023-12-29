  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)