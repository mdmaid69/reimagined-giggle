  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)