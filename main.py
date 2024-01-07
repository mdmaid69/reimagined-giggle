  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)