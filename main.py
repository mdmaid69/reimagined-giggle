  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)