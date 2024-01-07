import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)