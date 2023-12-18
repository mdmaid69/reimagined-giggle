  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)