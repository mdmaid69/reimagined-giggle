  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value