  import os
  def get_current_directory():
        return os.getcwd()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)