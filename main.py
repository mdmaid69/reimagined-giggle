import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)