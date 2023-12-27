  import os
  def split_path(path):
        return os.path.split(path)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)