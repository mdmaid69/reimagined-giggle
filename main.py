  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)