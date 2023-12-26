  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)