  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
  import numpy as np
  def calculate_standard_deviation(arr):
        return np.std(arr)