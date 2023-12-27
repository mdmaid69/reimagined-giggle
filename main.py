  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)