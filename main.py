  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)