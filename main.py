  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)