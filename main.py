  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)