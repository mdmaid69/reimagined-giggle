  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)